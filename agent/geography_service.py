from agent.snowflake_client import run_query


def get_county_fips(county_name):

    query = f"""
    SELECT COUNTY_FIPS
    FROM "2020_METADATA_CBG_FIPS_CODES"
    WHERE LOWER(COUNTY) LIKE LOWER('%{county_name}%')
    LIMIT 1
    """

    result = run_query(query)

    if len(result) == 0:
        return None

    return result.iloc[0]["COUNTY_FIPS"]