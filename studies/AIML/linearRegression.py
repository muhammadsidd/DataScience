from __future__ import absolute_import,division,print_function,unicode_literals
import re
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from six.moves import urllib
import six 
import tensorflow.compat.v2.feature_column as fc

# print(tf.__version__)
dftrain  =  pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv')
dfeval = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv')
# print(dftrain.head())
y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived') #remove from original df and return this column 
# print(dftrain.loc[0],y_train.loc[0])

def graphics(dftrain):
    dftrain.age.hist(bins=20)
    plt.show()
    dftrain['sex'].value_counts().plot(kind='barh')
    dftrain['class'].value_counts().plot(kind = 'barh')
    pd.concat([dftrain,y_train],axis=1).groupby('sex')['survived'].mean().plot(kind='barh').set_xlabel('% Survived')
    plt.show()

CATEGORICAL_COLUMNS = ['sex','n_siblings_spouses','parch','class','deck','embark_town','alone']
NUMERIC_COLUMNS = ['age','fare']

#Prerequsite for Linear Regression.
#Convert string category into simplied numberic values across the board. 
feature_columns = []
for feature_name in CATEGORICAL_COLUMNS:
    vocabulary = dftrain[feature_name].unique()
    # print(vocabulary)
    feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name,vocabulary))

for feature_name in NUMERIC_COLUMNS:
    feature_columns.append(tf.feature_column.numeric_column(feature_name,dtype=tf.float32))

# print(feature_columns)
#increase number of epochs for better accuracy
def make_input_fn(data_df,label_df,num_epochs=12,shuffle=True,batch_size=32):
    def input_function():
        ds =  tf.data.Dataset.from_tensor_slices((dict(data_df),label_df))
        if shuffle:
            df = ds.shuffle(1000)
        ds = ds.batch(batch_size).repeat(num_epochs)
        return ds
    return input_function

train_input_fn = make_input_fn(dftrain,y_train)
eval_input_fn = make_input_fn(dfeval,y_eval,num_epochs=1, shuffle=False)

#create best fit line
#TensorFlow by default will use all the cores available as one single machine. 
linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns) #train
linear_est.train(train_input_fn)
result = linear_est.evaluate(eval_input_fn) #get model stats by testing on testing data

# print(result['accuracy'])
result = list(linear_est.predict(eval_input_fn))
print(dfeval.loc[4])                    #did he survive in the given model
print(y_eval.loc[4])                    #did the person survive?
print(result[4]['probabilities'][1])    #probabilty of survival based on the model