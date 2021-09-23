# Databricks notebook source
from pyspark import SparkConf, SparkContext
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

conf = SparkConf().setAppName("RDD")
sc = SparkContext.getOrCreate(conf =  conf)

rdd =  sc.textFile('/FileStore/tables/StudentData.csv')

# COMMAND ----------

schema = StructType([
  StructField("age",IntegerType(),True),
  StructField("gender",StringType(),True),
  StructField("name",StringType(),True),
  StructField("course",StringType(),True),
  StructField("roll",StringType(),True),
  StructField("marks",IntegerType(),True),
  StructField("email",StringType(),True)
])

# COMMAND ----------

headers =  rdd.first()
rdd =  rdd.filter(lambda x : x!= headers).map(lambda x : x.split(','))
rdd = rdd.map(lambda x : [int(x[0]), x[1], x[2], x[3], x[4], int(x[5]), x[6]]) #map proper datatype for schema when converting data from rdd to df
rdd.collect()

# COMMAND ----------

rddToDf = rdd.toDF()

# COMMAND ----------

rddToDf.show()
columns = headers.split(',')
rddToDf =  rdd.toDF(columns)
rddToDf.printSchema()
rddToDf.show()

# COMMAND ----------

dfRdd = spark.createDataFrame(rdd,schema=schema)
dfRdd.printSchema()

# COMMAND ----------

dfRdd.show()

# COMMAND ----------


