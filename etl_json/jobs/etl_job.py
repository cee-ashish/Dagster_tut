from dagster import job
from etl_json.ops.extract import extract_data
from etl_json.ops.transform import transform_data
from etl_json.ops.load_sqlite import load_data
from etl_json.resources.sqllite_connection import sqlite_resource

@job(resource_defs={"sqlite_resource": sqlite_resource})
def my_etl_job():
    load_data(transform_data(extract_data()))
