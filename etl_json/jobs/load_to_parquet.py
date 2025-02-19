from dagster import job
from etl_json.ops.extract import extract_data
from etl_json.ops.transform import transform_data
from etl_json.ops.load_parquet import load_to_parquet
from etl_json.resources.parqet import parquet_resource

@job(resource_defs={"parquet_resource": parquet_resource})
def my_parquet_job():
    load_to_parquet(transform_data(extract_data()))