from .metadata_service import search_fields


def find_best_field(question: str):

    results = search_fields(question)

    if len(results) == 0:
        return None

    question = question.lower()

    for _, row in results.iterrows():

        title = str(row["TABLE_TITLE"]).lower()

        if question in title:
            return row["TABLE_ID"]

    return results.iloc[0]["TABLE_ID"]


def get_table_name(field_id: str):
    return f'2020_CBG_{field_id[:3]}'


