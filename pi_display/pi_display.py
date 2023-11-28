'''generic display class to be used as the basis for additional displays'''
import os
from PIL import Image,ImageDraw,ImageFont

red_chars = ["↑↑", "↓↓", "?", "-"]

class PiDisplay:
    '''Generic display class'''
    def __init__(self) -> None:
        self.imgdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'img')
        self.font30 = ImageFont.truetype(os.path.join(self.imgdir, 'Font.ttc'), 30)
        self.font60 = ImageFont.truetype(os.path.join(self.imgdir, 'Font.ttc'), 60)

    def update_reading(self, value, direction):
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
        self.draw(Blackimage, Redimage)

    def update_graph(self, image):
        pass

    def draw(self, black_image, red_image):
        raise Exception("Shouldn't call base class draw")