import os
import logging
from waveshare_epd import epd2in13b_V4
import time
from pi_display import PiDisplay

class EinkDisplay(PiDisplay):
    def __init__(self) -> None:
        super().__init__()
        logging.basicConfig(level=logging.DEBUG)
        logging.info("Initialising screen...")
        self.epd = epd2in13b_V4.EPD()
        self.epd.init()
        self.epd.clear()
        time.sleep(1)

    def __del__(self) -> None:
        logging.info("Clear...")
        self.epd.init()
        self.epd.clear()
        self.epd.sleep()

    def draw(self, black_image, red_image):
        self.epd.init()
        self.epd.display(self.epd.getbuffer(black_image.rotate(180)),
                         self.epd.getbuffer(red_image.rotate(180)))
        self.epd.sleep()