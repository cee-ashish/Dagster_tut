import json
from dagster import op , job

@op
def extract():
    with open("example_files/employee.json", "r") as f:
        data = json.load(f)
    return data