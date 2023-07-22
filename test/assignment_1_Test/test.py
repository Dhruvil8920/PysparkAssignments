from src.assignment_2.util import *
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql import SparkSession
import unittest
spark=SparkSession.builder.getOrCreate()
path = '../../resource/date_file.csv'
schema1=StructType([StructField("RechargeID",StringType(),True),
                   StructField("RechargeDate",IntegerType(),True),
                   StructField("RemainingDays",IntegerType(),True),
                   StructField("ValidityStatus",StringType(),True)])
df= spark.read.format('csv').schema(schema1).option('header', True).option('delimiter', ',').load(path)
df_date_updated=df.withColumn("changed_Recharge_date",to_date(col("RechargeDate"),"yyyyMMdd"))
df_drop_RechDate=df_date_updated.drop("RechargeDate")
class TestMyFunc(unittest.TestCase):
    if readCSV_to_df(path, schema1) is None:
        pass
    else:
        def test_1(self):
            try:
                result_df = readCSV_to_df(path,schema1)
                test_df = spark.read.format('csv').schema(schema1).option('header', True).option('delimiter', ',').load(path)
                self.assertEqual(result_df.show(), test_df.show())

            except AttributeError as e:
                print("test_1 fails", "AttributeError", e)
                raise
            else:
                print("test_1 passes")

    if create_new_column(df) is None:
        pass
    else:
        def test_2(self):
            try:
                result_df = create_new_column(df)
                df_date_updated= df.withColumn("changed_Recharge_date",to_date(col("RechargeDate"),"yyyyMMdd"))
                self.assertEqual(result_df.show(), df_date_updated.show())
                print("test_1 passes")

            except AssertionError:
                print("test_1 fails")
                raise

    if drop_column(df_date_updated) is None:
        pass
    else:
        def test_3(self):
            try:
                result_df = drop_column(df_date_updated)
                self.assertEqual(result_df.show(), df_drop_RechDate.show())
                print("test_1 passes")

            except AssertionError:
                print("test_1 fails")
                raise

   # if remove_duplicates(df_drop_RechDate) is None:
   #      pass
   #  else:
   #      def test_3(self):
   #          try:
   #              result_df = remove_duplicates(df_drop_RechDate)
   #              test_df = df_date_updated.drop("RechargeDate")
   #              self.assertEqual(result_df.show(), test_df.show())
   #              print("test_1 passes")
   #
   #          except AssertionError:
   #              print("test_1 fails")
   #              raise


if __name__ == '__main__':
    unittest.main()