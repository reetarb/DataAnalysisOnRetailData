#Import required packages and download the dataset
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#Read the csv file
#file is in different utf-8 
df = pd.read_csv('data.csv', encoding="latin1")
#Look for null values and Missing values in entire dataframe
df.isnull().sum()
df.dropna(subset=['CustomerID'], inplace=True)
df.isnull().sum()
#quantity cannot be negative, remove rows having -ve values(data cleaning)
#remove anamolies
df = df[df['Quantity'] >0 ]
df.describe()
#Data Transformation, create a col unit price for dollars
EURO_USD = 1.13
df['UnitPricein_USD'] = df['UnitPrice'].apply(lambda x:round(x*EURO_USD,2))
#To get a distribution(box plot) of total amount spent by Invoice
df['total_amount'] = df['Quantity'] * df['UnitPrice']
#df.head(3)
df_by_invoice = df.groupby(['InvoiceNo'],as_index=False)['total_amount'].sum()
df_by_invoice[df_by_invoice['total_amount']>1000].boxplot()

#df_by_invoice.head(3)
#df['df_by_invoice']
