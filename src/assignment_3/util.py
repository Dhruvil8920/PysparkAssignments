from pyspark.sql import SparkSession

# Nested Json file

''' Use 'feeds_json_data.json' file'''

# 1.Write custom schema and read the nested json file.
# 2.Explode the nested Json file into flattened json.
# 3.Check whether the data in nested json and flattened json are equal.
# 4.Replace the value of column “imagepaths”  from null to “replaced_val_image_path”.
# 5.Extract the date value from the column “createdAt” which is in timestamp format.
# 6.Extract the rows which has the ‘commentComment’ greater than 0.

#Read the nested json.
def readJSON_toDF(path):
    return 0

#Explode the Json file.
def explode_json(df):
    return 0

#Checking data with source data
def check_df(df):
    return 0

#Edit column
def edit_column(df):
    return 0

#Get date from timestamp
def get_date(df):
    return 0

#Filter data
def filter(df):
    return 0
