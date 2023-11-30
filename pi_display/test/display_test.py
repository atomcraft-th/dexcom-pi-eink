'''test module for eink display, initialise and display'''

import logging
import pytest
import time
from pi_display import PngDisplay

def test_display():
    logging.info("starting test")
    display = PngDisplay()
    display.update_reading(12, "↑")
    display.draw()
    display.update_reading(10, "↑↑")
    display.draw()
    display.update_reading(23.2, "→")
    display.draw()
    display.update_reading(2.2, "↓↓")
    display.draw()