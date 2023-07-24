from pyspark.sql import SparkSession

# Recharge details.
''' Use 'date_file.csv' file'''
# 1.Read the csv file with a custom schema by using the column names hint given in 'date_file.csv'.
# 2.Create a new column called “changed_Recharge_date” with 'Recharge date' column where the date values represented in yyyyMMdd(integer) change it into default date format (yyyy-MM-dd) with date DataType.
# 3.drop the ‘RechargeDate’ column.
# 4.Delete the duplicate rows.
# 5.Total Count of rows.
# 6.Add the “RemainingDays” column value to the date part of the column ”changed_Recharge_date” and remane this colummn as “expiryDate”.
# 7.Change the “over” value in 'ValidityStatus' column by a new value called “validity expired”.
# 8.Get the count of the column 'expiry_date' filtered based upon the date between "2020-05-12" and "2020-07-11".

#Reading a CSV file and Creating a dataframe.
def readCSV_to_df(path,schema):
    pass
    #return df

#Creating new column.
def create_new_column(df, name, datatype):
    pass
    #return df

#Drop the column.
def drop_column(df, name):
    pass
    #return df

#Removing duplicate row values.
def remove_duplicates(df):
    pass
    #return df

#Count the total rows.
def count_rows(df):
    pass
    #return count


#Creation of expiryDate column.
def expiry_date(df, colName1, colName2):
    pass
    #return df

#Changing value in the validity column (str1=value of column which we need to change, str2=value we need to set).
def change_value(df, name, str1, str2):
    pass
    #return df

#Filter the column
def count_date_based(df, name):
    pass
    #return df

