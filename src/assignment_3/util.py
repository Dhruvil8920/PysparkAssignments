from pyspark.sql import SparkSession

# Nested Json file

''' Use 'feeds_json_data.json' file'''

# 1.Write custom schema in the driver program and read the nested json file.
# 2.Explode the nested Json file into flattened json.
# 3.Check whether the data in nested json and flattened json are equal.
# 4.Replace the value of column “imagepaths”  from null to “replaced_val_image_path”.
# 5.Extract the date value from the column “createdAt” which is in timestamp format.
# 6.Extract the rows which has the ‘commentComment’ greater than 0.

#Read the nested json.
def readJSON_toDF(path,schema):
    pass
    #return df

#Explode the Json file.
def explode_json(df):
    pass
    #return df

#Checking data with source data
def check_df_data(df):
    pass
    #return df

#Edit column
def edit_column(df):
    pass
    #return df


#Get date from timestamp
def get_date(df):
    pass
    #return df

#Filter data
def filter(df):
    pass
    #return df
