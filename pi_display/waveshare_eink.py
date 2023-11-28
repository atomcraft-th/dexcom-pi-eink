import logging
from waveshare_epd import epd2in13b_V4
import time
from PIL import Image,ImageDraw,ImageFont
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

    def __delattr__(self, __name: str) -> None:
        super().__delattr__(__name)
        logging.info("Clear...")
        self.epd.init()
        self.epd.clear()

    def update_reading(self, value, direction_char):
        logging.info("drawing " + str(value) + " " + direction_char)
        Blackimage = Image.new('1', (self.epd.height, self.epd.width), 255)  # 250*122
        Redimage = Image.new('1', (self.epd.height, self.epd.width), 255)  # 250*122
        drawblack = ImageDraw.Draw(Blackimage)
        drawred = ImageDraw.Draw(Redimage)
        drawblack.text((10, 0), value + " " + direction_char, font = font30, fill = 0)
        drawred.text((10, 30), value + " " + direction_char, font = font30, fill = 0)
        self.epd.display(self.epd.getbuffer(Blackimage), self.epd.getbuffer(Redimage))
        self.epd.sleep()

    def update_graph(image):
        pass

