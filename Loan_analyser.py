#importing Packages pandas,math,mathplot and seaborn

import pandas as pd
import math as math
import matplotlib.pyplot as ploter
import seaborn as sns

#Reading the dataset into data frame data Path varies as per user storage

data=pd.read_csv("Loan_Data.csv")

#deleting unwanted Fields

del data['revol_util.1']
del data['int_rate.1']
del data['member_id']

#Viewing data info

data.info()

#Univarient analysis of Loan amount, Intrest rate, Annual income, Term and Installment

ploter.hist(data['loan_amnt'])
ploter.show()
ploter.hist(data['int_rate'])
ploter.show()
ploter.hist(data['annual_inc'])
ploter.show()
ploter.hist(data['term'])
ploter.show()
ploter.hist(data['installment'])
ploter.show()

#Bivarient Analysis using pyplot

ploter.scatter(data['annual_inc'],data['loan_amnt'],label="stars",color="red",marker=".",s=10)
ploter.xlabel("Annual income")
ploter.ylabel("Loan Amount")
ploter.show()

ploter.scatter(data['purpose'],data['installment'],label="stars",color="red",marker=".",s=10)
ploter.xlabel("purpose")
ploter.ylabel("Installment")
ploter.show()

ploter.scatter(data['home_OWNership'],data['loan_amnt'],label="stars",color="red",marker=".",s=10)
ploter.xlabel("Home Ownership")
ploter.ylabel("Loan Amount")
ploter.show()

ploter.scatter(data['loan_amnt'],data['loan_status'],label="stars",color="red",marker=".",s=10)
ploter.xlabel("Loan Amount")
ploter.ylabel("Loan Status")
ploter.show()

