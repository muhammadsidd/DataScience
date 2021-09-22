# Databricks notebook source
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("FilterData")
sc= SparkContext.getOrCreate(conf=conf)

# COMMAND ----------

rdd = sc.textFile('/FileStore/tables/movie_ratings.csv')

# COMMAND ----------

rdd.collect()

# COMMAND ----------

rdd2 = rdd.map(lambda x : (x.split(',')[0], int(x.split(',')[1])))

# COMMAND ----------

rdd2.collect()

# COMMAND ----------

rdd3 =  rdd2.reduceByKey(lambda x,y: x if x > y else y)

# COMMAND ----------

rdd3.collect()

# COMMAND ----------


