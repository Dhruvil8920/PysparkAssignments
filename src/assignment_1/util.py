from pyspark.sql import SparkSession

''' Use the transaction.csv and user.csv file.'''

# 1.Count of unique locations where each product is sold.
# 2.Find out the products bought by each user.
# 3.Total spending done by each user on each product.
# 4.Split the email id column into two columns based on '@' symbol and have the split values in two different columns such as “name” and “extension”.
# 5.list the user details who have bought items in a price range 10000-50000 along with product details.



#Reading a CSV file and Creating a dataframe.
def readCSV_to_DF(path):
    pass
    #return df

#Joining dataframes.
def join_two_DF(df1,df2,join_type):
    pass
    #return 0

#Function to count unique location.
def unique_location_count(df):
    pass
    #return 0

#Function to list the products bought by each user.
def user_products(df):
    pass
    #return 0

#Function to get the total spending by each user.
def total_spending(df):
    pass
    #return 0

#Split column.
def split(df):
    pass
    #return 0

#User details of the mentioned.
def user_details(df):
    pass
    #return 0

