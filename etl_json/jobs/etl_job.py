from dagster import job
from etl_json.ops.extract import extract
from etl_json.ops.transform import transform
from etl_json.ops.load import load

@job
def etl_job():
    data = extract()
    transformed_data = transform(data)
    load(transformed_data)