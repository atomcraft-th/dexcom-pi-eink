'''test module for eink display, initialise and display'''

from waveshare_epd import EinkDisplay
import pytest
import time

def test_value():
    display = EinkDisplay()
    display.update_reading(12, "↑")
    display.draw()
    time.sleep(30)
    display.update_reading(10, "↑↑")
    display.draw()
    time.sleep(30)
    display.update_reading(23.2, "→")
    display.draw()
    time.sleep(30)
    display.update_reading(2.2, "↓↓")
    display.draw()