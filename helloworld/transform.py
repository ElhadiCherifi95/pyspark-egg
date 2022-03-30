from pyspark.sql.functions import lit


def transform_column(df):
    return df.withColumn("transformed_col", lit("Transformed !"))
