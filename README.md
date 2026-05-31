# US Census Agent

A metadata-driven Census Question Answering Agent built using Snowflake, Python, and Streamlit.

The application allows users to ask natural language questions about US Census data and automatically:

- Identify the most relevant Census metric
- Determine the appropriate Census table
- Generate SQL dynamically
- Execute queries in Snowflake
- Display results, visualizations, and summary statistics

---

## Architecture

User Question
↓
Metadata Search
↓
Metric Selection
↓
Table Resolution
↓
Dynamic SQL Generation
↓
Snowflake Execution
↓
Results + Visualization

---

## Features

### Metadata-Driven Retrieval

Instead of hardcoding Census fields, the application searches Census metadata to identify relevant metrics dynamically.

### Dynamic SQL Generation

SQL queries are generated automatically based on the selected Census field and source table.

### Transparent Reasoning

The application displays:

- Selected metric
- Source table
- Generated SQL
- Reasoning steps

to help users understand how results were produced.

### Data Exploration

Users can:

- View query results
- Download results as CSV
- Explore visualizations
- Review summary statistics

---

## Example Questions

- population
- median household income
- poverty
- housing
- education
- age

---

## Project Structure

```text
SnowflakeFDE/
│
├── app.py
├── requirements.txt
├── README.md
│
└── agent/
    ├── metadata_service.py
    ├── sql_generator.py
    ├── question_answerer.py
    ├── snowflake_client.py
    ├── geography_service.py
    └── query_service.py
```

---

## Design Decisions

### Metadata First

The solution searches Census metadata rather than relying on hardcoded SQL queries.

### Dynamic Query Generation

The selected metric determines both the Census field and source table.

### Transparency

Generated SQL and reasoning steps are displayed to improve explainability.

### Modularity

Functionality is separated into dedicated services for:

- Metadata retrieval
- SQL generation
- Query execution
- Geography lookup
- Question answering

---

## Current Limitations

- Supports common Census concepts such as population, income, poverty, housing, education, and age.
- The current implementation selects the best matching metric rather than ranking multiple candidates.
- Geographic filtering is not currently implemented.
- Semantic search is keyword-based.

---

## Future Improvements

- Geographic filtering by state and county
- Ranking multiple candidate metrics
- Integration with Snowflake Cortex
- Conversational follow-up questions
- Improved semantic retrieval

---

## Technologies Used

- Snowflake
- Python
- Streamlit
- Pandas
- US Census Open Data
