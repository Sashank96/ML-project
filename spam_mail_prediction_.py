# -*- coding: utf-8 -*-
"""Spam_mail_Prediction .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JHfwuUQqPtpJ4IJTNwfb3oDQueUjZLqD

**SPAM MAIL DETECTION**

Firstly we are importing libraries

*   numpy is used to perform mathematical operations on arrays.
*   pandas is used to create data frames i.e; working with datasets by analysing the data.
*   TdidfVectorizer is used to convert the text data into featured vectors i.e., numericals values for training the machine in better way.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""The 1st major step is Loading and Preprocessing data"""

Initial_mail_data = pd.read_csv('/content/drive/MyDrive/Mail_data.csv')

print(Initial_mail_data)

# Replace the NULL values to NULL strings
Mail_data = Initial_mail_data.where((pd.notnull(Initial_mail_data)),'')

Mail_data.head()

Mail_data.shape

"""Label Encoding

In this case, Spam as 0, Ham as 1
"""

Mail_data.loc[Mail_data['Category'] == 'spam','Category',]=0
Mail_data.loc[Mail_data['Category'] == 'ham','Category',]=1
Mail_data.head()

# Choosing input and target variables

X = Mail_data['Message']
Y = Mail_data['Category']
X.head()

Y.head()

"""Splitting the data into train and test sets"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state =42)

"""Feature extraction"""

feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
# ignoring basic english words such as (is, the, and,....) and conerting all letters to lower case

X_train_features = feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)


# Making sure that target variable y is of type int
Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')

"""Training the model using Logistic Regression with training data"""

model = LogisticRegression()

model.fit(X_train_features,Y_train)

"""Evaluating the training model 1st with training data then with test data"""

Y_train_predict = model.predict(X_train_features)

# checking accuracy

Accuracy_trained_data = accuracy_score(Y_train, Y_train_predict)

print('Accuracy of model on trained data :', Accuracy_trained_data)

Y_test_predict = model.predict(X_test_features)

# checking accuracy

Accuracy_testing_data = accuracy_score(Y_test, Y_test_predict)

print('Accuracy of model on testing data :', Accuracy_testing_data)

"""Building predictive system

--Cheching for some random Input
"""

Input_mail =["You have buy for 1000 rupess cash, you will get free vouchers"]

# First convert to feature vectors
Input_data_features= feature_extraction.transform(Input_mail)

Mail_Type = model.predict(Input_data_features)

#print(Mail_Type)

if Mail_Type == 1 :
  print('Ham mail')
else :
  print('Spam')

