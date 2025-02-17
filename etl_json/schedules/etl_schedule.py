from dagster import ScheduleDefinition
from etl_json.jobs.etl_job import etl_job

etl_schedule = ScheduleDefinition(
    job=etl_job,
    cron_schedule="0 0 * * *"  
)