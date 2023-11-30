'''test for the readings from dexcom'''
from dexcom import ReadDexcom
import logging

def test_reading():
    dexcom_reader = ReadDexcom()
    logging.info("Read value " + str(dexcom_reader.get_reading()))
    logging.info("Read direction " + str(dexcom_reader.get_arrow()))
