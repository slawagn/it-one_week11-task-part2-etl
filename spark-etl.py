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

for table_name in ['books', 'authors', 'readers', 'loans', 'loan_books', 'book_readers']:
    df = spark.read \
        .format("jdbc")\
        .option("driver", "org.postgresql.Driver")\
        .option("url", f"jdbc:postgresql://{os.environ['POSTGRES_SRC_HOST']}:{os.environ['POSTGRES_SRC_PORT']}/{os.environ['POSTGRES_SRC_DB']}")\
        .option("dbtable", table_name)\
        .option("user", os.environ["POSTGRES_SRC_USER"])\
        .option("password", os.environ["POSTGRES_SRC_PASSWORD"])\
        .load()

    df \
        .write\
        .format("jdbc")\
        .option("driver", "org.postgresql.Driver")\
        .option("url", f"jdbc:postgresql://{os.environ['POSTGRES_DEST_HOST']}:{os.environ['POSTGRES_DEST_PORT']}/{os.environ['POSTGRES_DEST_DB']}")\
        .option("dbtable", table_name)\
        .option("user", os.environ["POSTGRES_DEST_USER"])\
        .option("password", os.environ["POSTGRES_DEST_PASSWORD"])\
        .mode("overwrite")\
        .save()
