'''bring together and display dexcom data'''

import sys
import time
from pi_display import PngDisplay
from dexcom import ReadDexcom


def main() -> int:
    """run the reading / display loop"""
    dexcom_reader = ReadDexcom()
    display = PngDisplay()
    display.update_reading(
        dexcom_reader.get_reading(),
        dexcom_reader.get_arrow()
    )
    display.draw()
    return 0

if __name__ == '__main__':
    sys.exit(main())
