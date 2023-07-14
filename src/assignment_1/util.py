from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

spark=SparkSession.builder.getOrCreate()
''' Use the transaction.csv and user.csv file.'''

# 1.Count of unique locations.
# Rename the resultant column as "Count_of_unique_location".
# 2.Find out the products bought by each user.
# Rename the resultant column as "products_bought".
# 3.Total spending done by each user on each product.
# Rename the resultant column as "total_spend".
# 4.Split the email id column into two columns based on '@' symbol.
# Have the split values in two different columns such as “name” and “extension”.
# 5.list the user details who have bought items in a price range 10000-50000 along with product details.



#Reading a CSV file and Creating a dataframe.
def readCSV_to_DF(path):
    pass
    #return df

#Joining dataframes.
def join_two_DF(df1,df2,join_type):
    pass
    #return df

#Function to count unique location.
def count_of_unique_location(df):
    pass
    #return df

#Function to list the products bought by each user.
def user_products(df):
    pass
    #return df

#Function to get the total spending by each user.
def total_spending(df):
    pass
    #return df

#Split column.
def split_column(df,delimiter,colName):
    pass
    #return df

#User details of the mentioned.
def user_details(df):
    pass
    #return df

