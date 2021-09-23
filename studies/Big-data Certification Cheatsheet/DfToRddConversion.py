# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, sum, avg, max, mean, count, udf
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType

spark = SparkSession.builder.appName("Spark DF actions").getOrCreate()

# COMMAND ----------

df =  spark.read.options(inferSchema = 'True', header = 'True').csv('/FileStore/tables/OfficeData.csv')

# COMMAND ----------

df.show()

# COMMAND ----------

rdd =  df.rdd
rdd.collect()

# COMMAND ----------

rdd.collect()

# COMMAND ----------

rdd.filter(lambda x : x[1] == 'Sales').collect()

# COMMAND ----------


