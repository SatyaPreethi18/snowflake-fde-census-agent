from .snowflake_client import run_query


def load_metadata():
    return run_query("""
        SELECT *
        FROM "2020_METADATA_CBG_FIELD_DESCRIPTIONS"
    """)


def search_fields(keyword: str):

    df = load_metadata()

    keyword = keyword.lower()

    keyword_map = {
    "population": "total population",
    "people": "total population",
    "residents": "total population",

    "income": "median household income",
    "household income": "median household income",
    "earnings": "median household income",
    "salary": "median household income",

    "poverty": "poverty",

    "housing": "housing",
    "homes": "housing",

    "education": "education",
    "school": "education",

    "age": "sex by age"
    }

    for k, v in keyword_map.items():
        if k in keyword:
            keyword = v
            break

    searchable_cols = [
        "TABLE_TITLE",
        "TABLE_TOPICS",
        "FIELD_LEVEL_1",
        "FIELD_LEVEL_2",
        "FIELD_LEVEL_3",
        "FIELD_LEVEL_4",
        "FIELD_LEVEL_5",
        "FIELD_LEVEL_6",
    ]

    mask = False

    for col in searchable_cols:
        if col in df.columns:
            mask = mask | df[col].astype(str).str.lower().str.contains(
                keyword,
                na=False
            )

    return df.loc[mask]

def get_field_details(field_id):

    query = f"""
    SELECT *
    FROM "2020_METADATA_CBG_FIELD_DESCRIPTIONS"
    WHERE TABLE_ID = '{field_id}'
    """

    return run_query(query)