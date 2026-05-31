from .sql_generator import (
    find_best_field,
    get_table_name
)

from .metadata_service import get_field_details
from .snowflake_client import run_query


def answer_question(question):

    field = find_best_field(question)

    if not field:
        return None

    metadata = get_field_details(field)

    table_name = get_table_name(field)

    query = f'''
    SELECT
        CENSUS_BLOCK_GROUP,
        "{field}"
    FROM "{table_name}"
    LIMIT 20
    '''

    data = run_query(query)
    data.columns = [
    "Census Block Group",
    metadata.iloc[0]["TABLE_TITLE"]
    ]
    generated_sql = query


    reasoning = f"""
    Question: {question}

    Step 1: Search Census metadata using the user's question.

    Step 2: Identify the closest matching Census metric.

    Selected Metric: {metadata.iloc[0]["TABLE_TITLE"]}

    Field ID: {field}

    Step 3: Determine the source table.

    Selected Table: {table_name}

    Step 4: Generate SQL dynamically and execute it in Snowflake.
    """



    return {
    "field": field,
    "metric": metadata.iloc[0]["TABLE_TITLE"],
    "table": table_name,
    "data": data,
    "sql": generated_sql,
    "reasoning": reasoning
    }