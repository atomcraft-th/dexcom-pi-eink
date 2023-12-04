'''bring together and display dexcom data'''

import sys
import time
from waveshare_epd import EinkDisplay
from dexcom import ReadDexcom
import logging

def main() -> int:
    """run the reading / display loop"""
    dexcom_reader = ReadDexcom()
    display = EinkDisplay()
    logging.basicConfig(level=logging.WARNING)
    while(True):
        try:
            display.update_graph(dexcom_reader.get_levels(60))
            display.update_reading(
                dexcom_reader.get_reading(),
                dexcom_reader.get_arrow()
            )
            display.draw()
        except Exception as inst:
            logging.warning(inst)
        time.sleep(60)
    return 0

if __name__ == '__main__':
    sys.exit(main())
