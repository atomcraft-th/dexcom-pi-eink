import os
import logging
from waveshare_epd import epd2in13b_V4
import time
from PIL import Image,ImageDraw,ImageFont
from pi_display import PiDisplay

red_chars = ["↑↑", "↓↓", "?", "-"]

class EinkDisplay(PiDisplay):
    def __init__(self) -> None:
        super().__init__()
        logging.basicConfig(level=logging.DEBUG)
        logging.info("Initialising screen...")
        self.epd = epd2in13b_V4.EPD()
        self.epd.init()
        self.epd.clear()
        self.font30 = ImageFont.truetype(os.path.join(self.imgdir, 'Font.ttc'), 30)
        self.font60 = ImageFont.truetype(os.path.join(self.imgdir, 'Font.ttc'), 60)
        time.sleep(1)

    def __del__(self) -> None:
        logging.info("Clear...")
        self.epd.init()
        self.epd.clear()
        self.epd.sleep()


    def update_reading(self, value, direction):
        logging.info("drawing " + str(value) + " " + direction)
        self.epd.init()
        Blackimage = Image.new('1', (self.epd.height, self.epd.width), 255)  # 250*122
        Redimage = Image.new('1', (self.epd.height, self.epd.width), 255)  # 250*122
        drawblack = ImageDraw.Draw(Blackimage)
        drawred = ImageDraw.Draw(Redimage)
        if (direction in red_chars):
            drawred.text((140, 20), direction, font = self.font60, fill = 0)
        else:
            drawblack.text((140, 20), direction, font = self.font60, fill = 0)
        if (value > 20 or value < 4):
            drawred.text((30, 20), str(value), font = self.font60, fill = 0)
        else:
            drawblack.text((30, 20), str(value), font = self.font60, fill = 0)
        self.epd.display(self.epd.getbuffer(Blackimage.rotate(180)), self.epd.getbuffer(Redimage.rotate(180)))
        self.epd.sleep()

    def update_graph(image):
        pass

