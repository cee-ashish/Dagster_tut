from dagster import Definitions
from etl_json.jobs.etl_job import my_etl_job
from etl_json.jobs.load_to_parquet import my_parquet_job
from etl_json.resources.sqllite_connection import sqlite_resource
from etl_json.resources.parqet import parquet_resource

defs = Definitions(
    jobs=[my_etl_job, my_parquet_job],
    resources={"sqlite_resource": sqlite_resource,
               "parquet_resource": parquet_resource},
)
