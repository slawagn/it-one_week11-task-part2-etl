import os
from pyspark import SparkConf
from pyspark.sql.session import SparkSession

# SRC_JDBC_URL = f"jdbc:postgresql://{os.environ['POSTGRES_SRC_HOST']}:{os.environ['POSTGRES_SRC_PORT']}/{os.environ['POSTGRES_SRC_DB']}"
# SRC_PROPERTIES = {
#     "user": os.environ['POSTGRES_SRC_USER'],
#     "password": os.environ['POSTGRES_SRC_PASSWORD'],
#     "driver": "org.postgresql.Driver"
# }
# DEST_JDBC_URL = f"jdbc:postgresql://{os.environ['POSTGRES_DEST_HOST']}:{os.environ['POSTGRES_DEST_PORT']}/{os.environ['POSTGRES_DEST_DB']}"
# DEST_PROPERTIES = {
#     "user": os.environ['POSTGRES_DEST_USER'],
#     "password": os.environ['POSTGRES_DEST_PASSWORD'],
#     "driver": "org.postgresql.Driver"
# }


conf = SparkConf()
spark = SparkSession.builder.config(conf=conf).getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

data = [
    ("Hello", "world")
]
cols = ["Key", "Value"]
df = spark.createDataFrame(data, cols)
df.show()


query.awaitTermination()
