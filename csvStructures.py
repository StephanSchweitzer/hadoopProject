import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType

spark = SparkSession.builder \
    .master("local").appName("hdfs_test").getOrCreate()

spark.sql("show databases").show()

electionsSchema = StructType() \
    .add("city", "string") \
    .add("no", "integer") \
    .add("type", "string") \
    .add("state", "string") \
    .add("candidate", "string") \
    .add("party", "string") \
    .add("electors", "string") \
    .add("votes", "string") \
    .add("turnout", "string") \
    .add("margin", "string") \
    .add("margin%", "string") \
    .add("year", "integer")

pollutionSchema = StructType() \
    .add("stn_code", "string") \
    .add("sampling_date", "string") \
    .add("state", "string") \
    .add("location", "string") \
    .add("agency", "string") \
    .add("type", "string") \
    .add("so2", "float") \
    .add("no2", "float") \
    .add("rspm", "float") \
    .add("spm", "float") \
    .add("location_monitoring_station", "string") \
    .add("pm2_5", "float") \
    .add("date", "string")

populationSchema = StructType() \
    .add("city", "string") \
    .add("year", "integer") \
    .add("total_households", "integer") \
    .add("total_population", "integer") \
    .add("total_male_population", "integer") \
    .add("total_female_population", "integer")

economicInfoSchema = StructType() \
    .add("state", "string") \
    .add("1990", "integer") \
    .add("1991", "integer") \
    .add("1992", "integer") \
    .add("1993", "integer") \
    .add("1994", "integer") \
    .add("1995", "integer") \
    .add("1996", "integer") \
    .add("1997", "integer") \
    .add("1998", "integer") \
    .add("1999", "integer") \
    .add("2000", "integer") \
    .add("2001", "integer") \
    .add("2002", "integer") \
    .add("2003", "integer") \
    .add("2004", "integer") \
    .add("2005", "integer") \
    .add("2006", "integer") \
    .add("2007", "integer") \
    .add("2008", "integer") \
    .add("2009", "integer") \
    .add("2010", "integer") \
    .add("2011", "integer") \
    .add("2012", "integer") \
    .add("2013", "integer") \
    .add("2014", "integer") \
    .add("2015", "integer") \
    .add("2016", "integer") \
    .add("2017", "integer") \
    .add("2018", "integer") \
    .add("2019", "integer") \
    .add("2020", "integer") \
    .add("2021", "integer") \
    .add("2022", "integer") \
    .add("category", "string")
