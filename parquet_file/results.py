import pandas as pd

df = pd.read_parquet("/home/root1/AshishSherawat/Sample_pipeline/parquet_file/output.parquet")
df.to_csv("result.csv")