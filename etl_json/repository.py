from dagster import Definitions
from etl_json.jobs.etl_job import etl_job
from etl_json.assets.asset import asset
from etl_json.schedules.etl_schedule import etl_schedule
from etl_json.resources.sqllite_connection import sqlite_resource

defs = Definitions(
    jobs=[etl_job],
    assets=[asset],
    schedules=[etl_schedule],
    resources={"my_user": sqlite_resource}
   
)