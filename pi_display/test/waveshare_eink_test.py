'''test module for eink display, initialise and display'''

from pi_display import EinkDisplay
import pytest
import time

def test_value():
    display = EinkDisplay()
    display.update_reading(12, "↑")
    time.sleep(30)
    display.update_reading(10, "↑↑")
    time.sleep(30)
    display.update_reading(23.2, "→")
    time.sleep(30)
    display.update_reading(2.2, "↓↓")