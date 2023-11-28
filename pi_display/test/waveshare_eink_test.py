'''test module for eink display, initialise and display'''

from pi_display import EinkDisplay
import pytest
import time

def test_value():
    display = EinkDisplay()
    display.update_reading(23, chr(0x2190))
    time.sleep(60)
    display.update_reading(10, chr(0x2190))
    time.sleep(60)