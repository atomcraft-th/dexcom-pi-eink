'''test module for eink display, initialise and display'''

from pi_display import PngDisplay
import pytest
import time

def test_display():
    display = PngDisplay()
    display.update_reading(12, "↑")
    display.draw
    display.update_reading(10, "↑↑")
    display.draw
    display.update_reading(23.2, "→")
    display.draw
    display.update_reading(2.2, "↓↓")