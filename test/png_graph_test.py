'''test to produce png graphs of dexcom data'''

import logging
import pytest
from pi_display import PngDisplay
from dexcom import ReadDexcom

def test_png_graph():
    logging.info("starting test")
    dexcom = ReadDexcom()
    display = PngDisplay()
    display.update_graph(dexcom.get_levels(60))
    display.update_reading(
        dexcom.get_reading(),
        dexcom.get_arrow()
    )
    display.draw()