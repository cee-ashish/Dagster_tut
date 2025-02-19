import json
from dagster import op

@op
def extract_data():
    with open("/home/root1/AshishSherawat/Sample_pipeline/example_files/employee.json", "r") as file:
        data = json.load(file)
    return data
