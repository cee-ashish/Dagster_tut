from dagster import op
import pandas as pd

@op(required_resource_keys={"parquet_resource"})
def load_to_parquet(context, data):
    output_dir = context.resources.parquet_resource
    output_file = f"{output_dir}/output.parquet"

    df = pd.DataFrame(data)
    df.to_parquet(output_file, engine="pyarrow", index=False)

    context.log.info(f"Data saved to Parquet at: {output_file}")