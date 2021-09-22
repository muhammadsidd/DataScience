# Databricks notebook source
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("FilterData")
sc= SparkContext.getOrCreate(conf=conf)

# COMMAND ----------

rdd = sc.textFile('/FileStore/tables/test3.txt')
rdd.collect()

# COMMAND ----------

rdd=  rdd.repartition(5)
rdd2 = rdd.flatMap(lambda x : x.split(" "))
rdd3 =  rdd2.map(lambda x: (x,1))

# COMMAND ----------

rdd3.saveAsTextFile('/FileStore/tables/output/5partitionOutput')

# COMMAND ----------

rdd4 = rdd3.coalesce(2)

# COMMAND ----------

rdd4.getNumPartitions()

# COMMAND ----------

rdd3.getNumPartitions()

# COMMAND ----------


