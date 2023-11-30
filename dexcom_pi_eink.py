'''bring together and display dexcom data'''

import sys
import time
from waveshare_epd import EinkDisplay
from dexcom import ReadDexcom


def main() -> int:
    """run the reading / display loop"""
    dexcom_reader = ReadDexcom()
    display = EinkDisplay()
    while(True):
        display.update_reading(
            dexcom_reader.get_reading(),
            dexcom_reader.get_arrow()
        )
        time.sleep(60)
    return 0

if __name__ == '__main__':
    sys.exit(main())
