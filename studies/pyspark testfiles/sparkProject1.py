# Databricks notebook source
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("FilterData")
sc= SparkContext.getOrCreate(conf=conf)

# COMMAND ----------

rdd = sc.textFile('/FileStore/tables/StudentData.csv')

# COMMAND ----------

rdd.collect()

# COMMAND ----------

headers = rdd.first()
rdd=  rdd.filter(lambda x: x!= headers)
rdd.count() #number of students 

# COMMAND ----------

rdd2 =  rdd.map(lambda x : (x.split(',')[1],int(x.split(',')[5])))

# COMMAND ----------

rdd2 =  rdd2.reduceByKey(lambda x,y: x+y)

# COMMAND ----------

rdd2.collect()

# COMMAND ----------

rdd.collect()

# COMMAND ----------

rdd3 =  rdd.filter(lambda x : int(x.split(',')[5]) >= 50)
rdd3.count()

# COMMAND ----------

courserdd =  rdd.map(lambda x: (x.split(',')[3],1))

# COMMAND ----------

courserdd.collect()

# COMMAND ----------

courserdd =  courserdd.reduceByKey(lambda x,y: x+y) #students per course 

# COMMAND ----------

enrolled = courserdd.collect() 
enrolled

# COMMAND ----------

courseMarks = rdd.map(lambda x: (x.split(',')[3],int(x.split(',')[5])))

# COMMAND ----------

courseMarks = courseMarks.reduceByKey(lambda x,y: x+ y)

# COMMAND ----------

total_marks=courseMarks.collect()
total_marks

# COMMAND ----------

avgmarks = rdd.map(lambda x: (x.split(',')[3],(int(x.split(',')[5]),1)))

# COMMAND ----------

avgmarks.collect()

# COMMAND ----------

avgmarks =  avgmarks.reduceByKey(lambda x,y: (x[0]+y[0],x[1]+y[1]))

# COMMAND ----------

avgmarks.collect()

# COMMAND ----------

avgmarks = avgmarks.map(lambda x: x[1][0]/x[1][1])

# COMMAND ----------

avgmarks.collect()

# COMMAND ----------

minmax = rdd.map(lambda x: (x.split(',')[3],int(x.split(',')[5])))
minmax.collect()

# COMMAND ----------

minmax = minmax.reduceByKey(lambda x,y : x if x > y else y)
minmax.collect()

# COMMAND ----------


