'''test for the readings from dexcom'''
from dexcom import ReadDexcom

def test_reading():
    dexcom_reader = ReadDexcom()
    print("Read value " + str(dexcom_reader.get_reading()))
    print("Read direction " + str(dexcom_reader.get_arrow()))
