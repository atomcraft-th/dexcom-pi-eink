'''test module for eink display, initialise and display'''

from display import EinkDisplay
import pytest

def test_value():
    display = EinkDisplay()
    display.update_reading(23, chr(2190))