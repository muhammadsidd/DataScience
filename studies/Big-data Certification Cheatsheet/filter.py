# Databricks notebook source
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("FilterData")
sc= SparkContext.getOrCreate(conf=conf)

# COMMAND ----------

rdd = sc.textFile("/FileStore/tables/quiz2.txt")

# COMMAND ----------

rdd.collect()

# COMMAND ----------

rdd2 = rdd.flatMap(lambda x: x.split(" "))

# COMMAND ----------

rdd2.collect()

# COMMAND ----------

rdd3 = rdd2.filter(lambda x: not (x.startswith('c') or x.startswith('a')))

# COMMAND ----------

rdd3.collect()

# COMMAND ----------


