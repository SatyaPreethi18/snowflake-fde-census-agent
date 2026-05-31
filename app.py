import streamlit as st
from agent.question_answerer import answer_question

st.set_page_config(page_title="US Census Agent")

st.title("🏛️ US Census Agent")

question = st.text_input(
    "Ask a Census Question",
    placeholder="What is the median household income?"
)

if st.button("Ask"):

    with st.spinner("Searching Census data..."):

        result = answer_question(question)

    if result is None:
        st.error("No matching Census metric found. Try income, population, poverty, housing, education, or age.")

    else:

        st.subheader("Question")
        st.write(question)

        st.subheader("Metric")
        st.success(result["metric"])

        st.subheader("Field ID")
        st.code(result["field"])

        st.subheader("Agent Reasoning")
        st.info(result["reasoning"])

        st.subheader("Design Assumptions")

        st.markdown("""
        - Questions are mapped to Census metadata rather than hardcoded SQL.
        - The best matching metric is selected from metadata search results.
        - SQL is generated dynamically using the selected Census field.
        - Results are retrieved directly from Snowflake.
        """)

        st.subheader("Design Decisions")

        st.markdown("""
        ### Metadata-Driven Retrieval

        Instead of hardcoding Census fields, the application searches Census metadata
        to identify relevant metrics dynamically.

        ### Dynamic SQL Generation

        Once a metric is selected, SQL is generated automatically based on the
        corresponding Census table and field.

        ### Transparency

        The generated SQL and reasoning steps are displayed so users can understand
        how the result was produced.
        """)


        st.subheader("Generated SQL")
        st.code(result["sql"], language="sql")

        st.subheader("Results")
        st.dataframe(result["data"])

        st.subheader("Visualization")
        st.bar_chart(
        result["data"].set_index("Census Block Group")
        )

        st.subheader("Quick Statistics")

        col = result["data"].iloc[:, 1]


        st.metric(
            "Average",
            f"{col.mean():,.0f}"
        )

        st.metric(
            "Maximum",
            f"{col.max():,.0f}"
        )

        st.metric(
            "Minimum",
            f"{col.min():,.0f}"
        )

        st.subheader("Current Limitations")

        st.markdown("""
        - Supports common Census concepts such as population, income, poverty, housing, education, and age.
        - The current implementation selects the best matching metric rather than ranking multiple candidates.
        - Geographic filtering is not currently implemented.
        - More advanced natural language interpretation could be added using Snowflake Cortex or LLMs.
        """)

        st.markdown("---")

        st.caption("""Built with:

        • Snowflake
        • Python
        • Streamlit
        • Metadata-driven SQL generation
        • US Census Open Data
        """)

        csv = result["data"].to_csv(index=False)

        st.download_button(
            label="Download Results",
            data=csv,
            file_name="census_results.csv",
            mime="text/csv"
        )