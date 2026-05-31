# US Census Agent

## Live Demo

https://app-fde-census-agent-7zlvukzzappjtjjtk9espnu.streamlit.app

## Overview

US Census Agent is a metadata-driven question answering application built using Snowflake, Python, and Streamlit.

The application enables users to ask natural language questions about US Census data and automatically:

* Identify the most relevant Census metric
* Determine the appropriate Census table
* Generate SQL dynamically
* Execute queries in Snowflake
* Display results, visualizations, and summary statistics

---

## Architecture

```text
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
Snowflake Query Execution
      ↓
Results + Visualization
```

---

## Features

### Metadata-Driven Retrieval

Instead of relying on hardcoded Census fields, the application searches Census metadata to identify the most relevant metric dynamically.

### Dynamic SQL Generation

SQL queries are generated automatically based on the selected Census field and associated source table.

### Transparent Reasoning

To improve explainability, the application displays:

* Selected metric
* Source table
* Generated SQL
* Agent reasoning steps

### Data Exploration

Users can:

* View query results
* Download results as CSV
* Explore visualizations
* Review summary statistics

---

## Example Questions

* population
* median household income
* poverty
* housing
* education
* age

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
    └── geography_service.py
```

---

## Design Decisions

### Metadata-First Approach

The solution searches Census metadata rather than relying on predefined SQL queries. This allows the application to dynamically identify relevant Census metrics.

### Dynamic Query Generation

The selected metric determines both the Census field and the source table used to generate SQL.

### Transparency

Generated SQL and reasoning steps are displayed to help users understand how answers are produced.

### Modular Design

Functionality is separated into dedicated components for:

* Metadata retrieval
* SQL generation
* Snowflake query execution
* Geography lookup
* Question answering

---

## Current Limitations

* Supports common Census concepts such as population, income, poverty, housing, education, and age.
* The current implementation selects the best matching metric rather than ranking multiple candidate metrics.
* Geographic filtering is not currently implemented.
* Semantic search is keyword-based.

---

## Future Improvements

* Geographic filtering by state and county
* Ranking multiple candidate metrics
* Integration with Snowflake Cortex
* Conversational follow-up questions
* Improved semantic retrieval

---

## Reflection

Given the 24-hour time constraint, I prioritized building a working end-to-end system that demonstrates metadata-driven retrieval, dynamic SQL generation, Snowflake integration, and transparent reasoning.

I intentionally focused on the core agent workflow rather than advanced user interface features. Time was invested in ensuring that user questions could be mapped to Census metadata, translated into SQL dynamically, executed against Snowflake, and explained to the user.

Several improvements were intentionally left out:

- Ranking multiple candidate metrics instead of selecting a single best match
- Geographic filtering and location-aware queries
- Semantic retrieval using embeddings or Snowflake Cortex
- More sophisticated handling of ambiguous questions
- Production-grade monitoring, logging, and testing

If additional time were available, I would focus first on improving retrieval quality and ambiguity handling, since these would have the greatest impact on user experience and answer accuracy.

---

## Technologies Used

* Snowflake
* Python
* Streamlit
* Pandas
* US Census Open Data
