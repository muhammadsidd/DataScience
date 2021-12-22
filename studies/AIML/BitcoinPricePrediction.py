# The intent of this program is to predict the price of Bitcoin.
# The model will take 180 days of pricing data and calculate
# the relative future value of the bitcoin

from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.models import Sequential

crypto_currency = 'BTC'
against_currency = 'USD'

start = dt.datetime(2016, 1, 1)
end = dt.datetime.now()

# web scrape the yahoo API and get the stock details in a dataframe
data = web.DataReader(
    f'{crypto_currency}-{against_currency}', 'yahoo', start, end)


################### DATA PREPROCESSING ############################

# STEP 1
# squeeze all the values between 0 and 1
scaler = MinMaxScaler(feature_range=(0, 1))
# STEP 2
# Transform current data column into 0,1 relative values
# -1 becuz its an unknown dimension and we want compatibiity
scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1, 1))

# STEP 3
# set prediction length
prediction_days = 360
future_day = 30 # predict next 30 days 
#historic, predictive
x_train, y_train = [], []
# populate the dataset with respective value
for x in range(prediction_days, len(scaled_data)-future_day):
    # training model for hostoric data
    x_train.append(scaled_data[x-prediction_days:x, 0])
    y_train.append(scaled_data[x+future_day, 0])  # the day of prediction
# STEP 5
    # reshape the array to fit in another dimension
x_train, y_train = np.array(x_train), np.array(
    y_train)  # Better format - turning into numpy array
# add one more dimension
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

################### CREATE NEURAL NETWORK ############################
# if problem occurs pip insall numpy==1.19.5

model = Sequential()

model.add(LSTM(units=50, return_sequences=True, input_shape = (x_train.shape[1],1)))
model.add(Dropout(0.2))
model.add(LSTM(units=50,return_sequences=True))
model.add(Dropout(0.2)) #Dropout prevents overfitting of the model
model.add(LSTM(units=50))
model.add(Dropout(0.2))
model.add(Dense(units=1))

model.compile(optimizer='adam',loss = 'mean_squared_error')
model.fit(x_train,y_train, epochs = 25, batch_size=32)

##################### TESTING THE MODEL ##############################

test_start =  dt.datetime(2020,1,1)
test_end =  dt.datetime.now()

test_data = web.DataReader(
    f'{crypto_currency}-{against_currency}', 'yahoo', test_start, test_end)

actual_price = test_data['Close'].values

total_dataset =  pd.concat((data['Close'], test_data['Close']), axis = 0)

model_inputs = total_dataset[len(total_dataset) -  len(test_data) - prediction_days:].values
model_inputs = model_inputs.reshape(-1,1)
model_inputs =  scaler.fit_transform(model_inputs)

x_test = []

for x in range(prediction_days, len(model_inputs)):
    x_test.append(model_inputs[x-prediction_days:x,0])

x_test = np.array(x_test)
x_test =  np.reshape(x_test, (x_test.shape[0], x_test.shape[1],1))

prediction_prices = model.predict(x_test)
prediction_prices = scaler.inverse_transform(prediction_prices)

plt.plot(actual_price, color = 'black', label = 'Actual Prices')
plt.plot(prediction_prices, color = 'red', label = 'Predicted Prices')
plt.title(f'{crypto_currency} Price Prediction')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend(loc = 'upper left')
plt.show()


#################### PREDICTITION FOR NEXT 30 DAYS ######################

real_data = [model_inputs[len(model_inputs) + 1 - prediction_days:len(model_inputs) + 1, 0]]
real_data = np.array(real_data)
real_data =  np.reshape(real_data, (real_data.shape[0], real_data.shape[1],1))

prediction = model.predict(real_data)
prediction = scaler.inverse_transform(prediction)
print(prediction)