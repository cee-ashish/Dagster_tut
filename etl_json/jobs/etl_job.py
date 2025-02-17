from dagster import job
from etl_json.ops.extract import extract
from etl_json.ops.transform import transform
from etl_json.ops.load import load
from etl_json.resources.sqllite_connection import sqlite_resource  # ✅ Import the resource

@job(resource_defs={"db": sqlite_resource})  # ✅ Register the SQLite resource
def etl_job():
    data = extract()
    transformed_data = transform(data)
    load(transformed_data)
