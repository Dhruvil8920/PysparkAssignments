from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Define your data
data = [("1",), ("2",), ("3",)]  # A list of tuples

# Define the schema
schema = ["no"]  # A list of column names

def createDF(data,schema):
    # Create a DataFrame
    df = spark.createDataFrame(data, schema)
    return df

def trial(var):
    pass

df = createDF(data,schema)
df.show()