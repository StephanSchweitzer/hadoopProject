import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType
import csvStructures as csv_struc
import sillyFunctions as ezFunc


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # electiondata = csv_struc.spark.read.csv(
    #     "hdfs://localhost:9000/user/steez/indianElections/Loksabha_1962-2019.csv",
    #     schema=csv_struc.electionsSchema)
    #
    # electiondata.show(5)

    # polutiondata = csv_struc.spark.read.csv(
    #     "hdfs://localhost:9000/user/steez/pollution/data.csv",
    #     schema=csv_struc.polutionSchema)
    #
    # polutiondata.show(5)

    # economic_info_data = csv_struc.spark.read.csv(
    #     "hdfs://localhost:9000/user/steez/socioEconomicData/india.csv",
    #     schema=csv_struc.economicInfoSchema)
    #
    # economic_info_data.show(5)

    # population_data_2001 = csv_struc.spark.read.csv(
    #     "hdfs://localhost:9000/user/steez/populationCensusByYear/data_2001.csv",
    #     schema=csv_struc.populationSchema)
    #
    # population_data_2001.show(5)

    # %%
    # all_population_data = csv_struc.spark.read.csv(
    #     "hdfs://localhost:9000/user/steez/populationCensusByYear/all_years.csv",
    #     schema=csv_struc.populationSchema)
    #
    # all_population_data.describe().show()

    print(ezFunc.givethegoodyear(1211009))

    # spark = SparkSession.builder \
    #     .master("local").appName("hdfs_test").getOrCreate()
    #
    # spark.sql("show databases").show()

# %% next
    import sillyFunctions as ezFunc
    #print(ezFunc.givethegooddate('12-12-15'))





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
