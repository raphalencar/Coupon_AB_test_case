import pyspark.sql.functions as f
from pyspark.sql.types import TimestampType, DateType, FloatType, DoubleType, LongType, ArrayType, IntegerType

def cast_to_timestamp(df, columns):
    for col_name in columns:
        if col_name in df.columns and df.schema[col_name].dataType not in (TimestampType(), DateType()):
            df = df.withColumn(col_name, f.to_timestamp(f.col(col_name)))
    return df

def cast_to_float(df, columns):
    for col_name in columns:
        if col_name in df.columns and df.schema[col_name].dataType != FloatType():
            df = df.withColumn(col_name, f.col(col_name).cast(FloatType()))
    return df

def cast_to_double(df, columns):
    for col_name in columns:
        if col_name in df.columns and df.schema[col_name].dataType != DoubleType():
            df = df.withColumn(col_name, f.col(col_name).cast(DoubleType()))
    return df

def cast_to_long(df, columns):
    for col_name in columns:
        if col_name in df.columns and df.schema[col_name].dataType != LongType():
            df = df.withColumn(col_name, f.col(col_name).cast(LongType()))
    return df

def json_column_parse(df, column_name, schema):
    if column_name in df.columns:
        print(f"Transformando a coluna {column_name} do tipo StringType para ArrayType(StructType) usando from_json e schema explícito.")

        cleaned_col = f.regexp_replace(f.col("items"), r'\\"', '"')
        
        return df.withColumn(f"{column_name}_parsed", f.from_json(cleaned_col, ArrayType(schema)))
    
def add_column_comments(table_name, comments_dict):
    for col_name, comment_text in comments_dict.items():
        safe_comment = comment_text.replace('"', '\\"')
        
        sql_command = f"""
        ALTER TABLE {table_name} ALTER COLUMN {col_name} COMMENT "{safe_comment}"
        """
        spark.sql(sql_command)
