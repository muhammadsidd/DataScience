# Databricks notebook source
from pyspark.sql import SparkSession 
from pyspark.sql.types import StructType, StructField, StringType,IntegerType
spark = SparkSession.builder.appName('SparkDfs').getOrCreate()

# COMMAND ----------

schema = StructType([
  StructField("age", IntegerType(),True),
  StructField("gender", StringType(),True),
  StructField("name", StringType(),True),
  StructField("course", StringType(),True),
  StructField("roll", StringType(),True),
  StructField("marks", IntegerType(),True),
  StructField("email", StringType(),True)                       
                    ])
df = spark.read.options(header='True',).schema(schema).csv('/FileStore/tables/StudentData.csv') 

# COMMAND ----------

df.show()
df.printSchema()

# COMMAND ----------


