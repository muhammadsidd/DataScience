# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, sum, avg, max, mean, count, udf
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

spark = SparkSession.builder.appName("Spark DF actions").getOrCreate()

# COMMAND ----------

ratingdf = spark.read.options(header ='True', inferSchema = "True").csv('/FileStore/tables/ratings.csv')
moviesdf =spark.read.options(header ='True', inferSchema = "True").csv('/FileStore/tables/movies.csv')
ratingdf.cache()
moviesdf.cache()

# COMMAND ----------

ratingdf.show()
moviesdf.show()


# COMMAND ----------

display(moviesdf)


# COMMAND ----------

display(ratingdf)

# COMMAND ----------

ratingdf.join(moviesdf, "movieId", 'left').show()

# COMMAND ----------

(train,test) = ratingdf.randomSplit((0.8,0.2)) #train data on 80% and test on 20%

# COMMAND ----------

train.show()
train.count()

# COMMAND ----------

test.show()
test.count()

# COMMAND ----------

als = ALS(userCol="userId", itemCol="movieId", ratingCol="rating", nonnegative=True,implicitPrefs=False, coldStartStrategy="drop") #specifications for training 
#userCol =  columns for the users who have provided the rating 
#itemCol = what do you want to recommend
#ratingCol =  based on what data
#nonnegative = do we need to cosider the non negative?
#implicit =  no our data is explicit, users have provided the rating (active)
#coldstartStrategy =  what to do with people who have not provided rating for the movie? drop them

# COMMAND ----------

#HYPERPARAMETER TUNING AND CROSS VALIDATION (OPTIMIZATION)

param_grid =  ParamGridBuilder().addGrid(als.rank,[10,50,100,150]).addGrid(als.regParam, [.01,0.05, 0.1, .15]).build() #16 models with all these combination of parameters 

# COMMAND ----------

evaluator = RegressionEvaluator(metricName="rmse",labelCol = "rating", predictionCol="prediction") #parameters for evaluating 16 models weightage of the movie is taken into account using the rating 

# COMMAND ----------

cv = CrossValidator(estimator=als,estimatorParamMaps=param_grid,evaluator=evaluator,numFolds =5) 
#considers the evaluator (als model we created) with all the 16 models generated (param_grid) and provide the best match based on the parameters (evaluator) and check this 5 times to confirm and optimize

# COMMAND ----------

model =  cv.fit(train) #provides the best suitable model based on the paramgrid and Regression Evaluator for the training model (in other words, this is how the train df should look like)
bestModel = model.bestModel #pick the best out of the 16 models
testPredictions = bestModel.transform(test) #based on train dataset it will make some recommendations on the test model
RMSE = evaluator(testPredictions) #actual error 
print(RSME) #The actual approval % of the best fit 

# COMMAND ----------

#1,["A","B","C"]
#explode will give u 
#1,A
#1,B
#1,C
recommendations = recommendation = best_model.recommendedForAllUsers(5) #cosiders best model looks at top 5 recommendations per user
df = recommendations
display(df)
df2 = df.withColumn("movieid_rating",explode("recommendations")) #explode recommendation column 
display(df2)
display(d2.select("usedId", col("movieid_rating.movieId"),col("movie_rating.rating"))) #5 recommended movie for every user and their estimated rating 

# COMMAND ----------


