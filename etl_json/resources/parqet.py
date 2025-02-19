from dagster import resource
import os

@resource
def parquet_resource(init_context):
    output_dir = "parquet_file"  
    os.makedirs(output_dir, exist_ok=True)
    return output_dir