# Databricks notebook source
from pyspark import SparkConf, SparkContext
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit
# conf = SparkConf().setAppName("RDD")
# sc = SparkContext.getOrCreate(conf =  conf)

spark = SparkSession.builder.appName("SparkDataFramee").getOrCreate()


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

df = spark.read.options(header = "True").schema(schema).csv('/FileStore/tables/StudentData.csv')

# COMMAND ----------

df.show()

# COMMAND ----------

df.select('gender','name').show()

# COMMAND ----------

df.select(df.name, df.email).show()

# COMMAND ----------

df2 = df.select(col("roll"),col("name")).show() #filter the data and only show selected column in a new df

# COMMAND ----------

df.columns

# COMMAND ----------

df.select(df.columns[:5:2]).show()

# COMMAND ----------

#With Column
df2 = df.withColumn("roll",col("roll").cast("String")) #convert the datatype of a column, need to capture it in a new data frame since its a transformation 

# COMMAND ----------

df2.show()
df2.printSchema()

# COMMAND ----------

#adding a new cell
d3 =  df2.withColumn("marks",col("marks").cast("String"))

# COMMAND ----------

d3.printSchema()

# COMMAND ----------

df2.printSchema()

# COMMAND ----------

df3 = df2.withColumn("marks",col("marks")+20) #adding 20 points to the entire column

# COMMAND ----------

df3.show()

# COMMAND ----------

#creating a new column
dfnew =  df3.withColumn("aggregated markes", col('marks')-20)

# COMMAND ----------

dfnew.show()

# COMMAND ----------

#create a new independent column 
df = df.withColumn("country",lit("USA")) #lit to add new values for each row in the country column 

# COMMAND ----------

df.show()

# COMMAND ----------

#adding and updating multipe columns 
dfmax = df.withColumn("marks",col("marks")+10).withColumn("updated Marks", col("marks")-25).withColumn("Country2", lit("Pakistan"))

# COMMAND ----------

dfmax.show()

# COMMAND ----------

dfmax = dfmax.withColumnRenamed("gender","sex")

# COMMAND ----------

dfmax.show()

# COMMAND ----------

df1 = df.filter(col("course") == "DB")

# COMMAND ----------

df2 = df1.filter((df.course == "DB") & (col("marks")> 50)) # can use or '|'

# COMMAND ----------

 df2.show()

# COMMAND ----------

courses = ['DB','Cloud','PF']
df3  =  dfmax.filter(df.course.isin(courses))

# COMMAND ----------

df3.show()

# COMMAND ----------

#starts With API
#endswith
df99 = dfmax.filter(dfmax.course.startswith("D"))
df98 =  dfmax.filter(df.course.endswith("B"))
df97 = dfmax.filter(df.name.startswith("Hubert"))
df99.show()
df98.show()
df97.show()

# COMMAND ----------

df.show()

# COMMAND ----------

df =  df.withColumn("totalmarks", lit(120))

# COMMAND ----------

df.show()

# COMMAND ----------

df = df.withColumn("percentage", col("marks")/col("totalmarks")*100)

# COMMAND ----------

df.show()

# COMMAND ----------


