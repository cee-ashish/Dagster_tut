from dagster import op, job

@op
def transform(data):
    result = [record for record in data if record["name"] == "John Doe"]

    return result if result else None