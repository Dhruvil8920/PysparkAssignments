from pyspark.sql import SparkSession

# Recharge details.
''' Use 'date_file.csv' file'''
# 1.Read the csv file with a custom schema by using the column names hint given in 'date_file.csv'.
# 2.Create a new column called “changed_Recharge_date” which has Recharge date column date values represented in yyyy-MM-dd default date format.Also change the data type to date type.
# 3.drop the ‘RechargeDate’ column.
# 4.Delete the duplicate rows.
# 5.Total Count of rows.
# 6.Add the “RemainingDays” column value to the date part of the column ”changed_Recharge_date” and give the newly calculated date in a column called “expiryDate”.
# 7.Change the “over” value in ValidityStatus column by a new value called “validity expired”.
# 8.Get the count of the column 'expiry_date' filtered based upon the date between "2020-05-12" and "2020-07-11".

#Reading a CSV file and Creating a dataframe.
def readCSV_to_df(path,schema):

    a= "hello"
    return a
def readCSV_to_df(path, schema):
    pass
    # return df

#Creating new column.
def create_new_column(df):
    pass
    #return df

#Drop the column.
def drop_column(df):
    pass
    #return df

#Removing duplicate row values.
def remove_duplicates(df):
    pass
    #return df

#Count the total rows.
def count_rows(df):
    pass
    #return df


#Creation of expiry Date column.
def expiry_date(df):
    pass
    #return df

#Changing value in the validity column.
def change_value(df):
    pass
    #return df

#Filter the column
def count_date_based_(df):
    pass
    #return df

