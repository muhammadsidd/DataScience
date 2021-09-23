# Databricks notebook source
from pyspark import SparkConf, SparkContext


# COMMAND ----------

conf = SparkConf().setAppName("Quiz")
sc = SparkContext.getOrCreate(conf=conf)

# COMMAND ----------

rdd1 = sc.textFile('/FileStore/tables/quiz1.txt')

# COMMAND ----------

def length(x):
  l1=x.split(' ')
  l2 = []
  for word in l1:
    l2.append(len(word))
  
  return l2

list = rdd1.collect() ##rdd2 is a list not rdd
list#will return a list

# COMMAND ----------

rdd2=rdd1.map(length)
#ALTERNATIVELY we can use this
# rdd2 = rdd1.map(lambda x: [len(s) for s in x.split(" ")])
rdd2.collect()

# COMMAND ----------


