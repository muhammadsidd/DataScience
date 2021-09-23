# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, sum, avg, max, mean, count, udf
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType

spark = SparkSession.builder.appName("Spark DF actions").getOrCreate()

# COMMAND ----------

df =  spark.read.options(inferSchema = 'True', header = 'True').csv('/FileStore/tables/StudentData.csv')

# COMMAND ----------

df.show()

# COMMAND ----------

df.createOrReplaceTempView("Student")

# COMMAND ----------

spark.sql("select name,course from Student where age > 28 and course == 'DB'").show()

## THIS STATEMENT IS EQUAVALENT TO 

df.select("name","course").filter((df.course == "DB") & (col("age")> 28)).show()

# COMMAND ----------

spark.sql("select course,gender, count(*) from Student where age > 28 group by course,gender").show()

df.filter(col("age")> 28).groupBy(col("course"), col("gender")).count().show()

# COMMAND ----------


