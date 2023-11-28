'''functions for interacting with dexcom interface'''

import os
from pydexcom import Dexcom
from datetime import timedelta, datetime
import logging

class ReadDexcom:
    '''dexcom handling class'''
    def __init__(self) -> None:
        login_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'passwd')
        with open(login_file, 'r') as pf:
            lines = pf.read().splitlines()
        self.dexcom = Dexcom(lines[0], lines[1], ous=True)
        self.glucose_reading = self.dexcom.get_current_glucose_reading()
        self.last_read = datetime.now()

    def get_reading(self):
        self.read_dexcom()
        return self.glucose_reading.mmol_l

    def get_arrow(self):
        self.read_dexcom()
        return self.glucose_reading.trend_arrow

    def read_dexcom(self):
        if ((datetime.now() - self.last_read).seconds >= 59):
            logging.info("reading glucose")
            self.glucose_reading = self.dexcom.get_current_glucose_reading()
            self.last_read = datetime.now()