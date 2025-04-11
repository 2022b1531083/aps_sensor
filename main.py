from Sensor.exception import SensorException
import os 
import sys

from Sensor.logger import logging
from Sensor.utils import dump_csv_file_to_mongodb_collection

# def test_exception():
#     try:
#         logging.info("ki yaha p bhaiaa ek error ayegi diveision by zero wali error ")
#         a=1/0
#     except Exception as e:
#        raise SensorException(e,sys) 




if __name__ == "__main__":
    
    file_path=r"C:\Users\91844\Desktop\live_sensor_project\aps_failure_training_set1.csv"
    database_name="APS_database"
    collection_name="sensor"
    dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name)

#     try:
#         test_exception()
#     except Exception as e:
#         print(e)