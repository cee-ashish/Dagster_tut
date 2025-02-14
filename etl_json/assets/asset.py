import json
from dagster import asset

@asset
def asset():
    
    file_path = 'example_files/employee.json'

   
    with open(file_path, 'r') as f:
        data = json.load(f)

    
    return data