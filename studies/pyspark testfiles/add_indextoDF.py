from pyspark.sql import SparkSession, functions as F
from pyspark import SparkConf
conf = SparkConf()

spark = SparkSession.builder \
        .config(conf=conf) \
        .appName('Dataframe with Indexes') \
        .getOrCreate()


# create a simple dataframe with two columns
data = [{'column1': 1, 'column2': 2}, {'column1': 15, 'column2': 21}]
df = spark.createDataFrame(data)
df.show()
'''+ - - - -+ - - - -+
|column1|column2 |
+ - - - -+ - - - -+
| 1     | 2      |
| 15    | 21     |
+ - - - -+ - - - -+'''

# use zipWithIndex to add the indexes and then toDF to get back to a dataframe
rdd_df = df.rdd.zipWithIndex()
df_final = rdd_df.toDF()
df_final.show()
'''+--------+---+
|      _1| _2|
+--------+---+
|  [1, 2]|  0|
|[15, 21]|  1|
+--------+---+'''

# Let's inspect the result datatypes:
df_final
#DataFrame[_1: struct<column1:bigint,column2:bigint>, _2: bigint, index: bigint]

# and then expand _1 column into the two we had before:
df_final = df_final.withColumn('column1', df_final['_1'].getItem("column1"))
df_final = df_final.withColumn('column2', df_final['_1'].getItem("column2"))

# finally select the columns we need:
df_final.select('index', 'column1', 'column2').show()
'''+-----+-------+-------+
|index|column1|column2|
+-----+-------+-------+
|    0|      1|      2|
|    1|     15|     21|
+-----+-------+-------+'''