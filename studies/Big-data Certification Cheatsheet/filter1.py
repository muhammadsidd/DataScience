# Databricks notebook source
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("FilterData")
sc= SparkContext.getOrCreate(conf=conf)

# COMMAND ----------

rdd = sc.textFile("/FileStore/tables/quiz2-1.txt")

# COMMAND ----------

rdd.collect()

# COMMAND ----------

rdd2 = rdd.flatMap(lambda x: x.split(" "))

# COMMAND ----------

rdd2.collect()

# COMMAND ----------

rdd3 = rdd2.filter(lambda x: not (x[0]=='a' or x[0]=='c'))

# COMMAND ----------

rdd3.collect()

# COMMAND ----------


