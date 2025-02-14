from dagster import Definitions
from etl_json.jobs.etl_job import etl_job
from etl_json.assets.asset import asset
from etl_json.schedules.etl_schedule import etl_schedule

defs = Definitions(
    jobs=[etl_job],
    assets=[asset],
    schedules=[etl_schedule],
   
)