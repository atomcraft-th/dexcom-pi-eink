'''generic display class to be used as the basis for additional displays'''
import os
from PIL import Image,ImageDraw,ImageFont

red_chars = ["↑↑", "↓↓", "?", "-"]

class PiDisplay:
    '''Generic display class'''
    def __init__(self, width, height) -> None:
        self.imgdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'img')
        self.font30 = ImageFont.truetype(os.path.join(self.imgdir, 'Font.ttc'), 30)
        self.font60 = ImageFont.truetype(os.path.join(self.imgdir, 'Font.ttc'), 60)
        self.width = width
        self.height = height
        self.black_img = Image.new('1', (self.width, self.height), 255)
        self.red_img = Image.new('1', (self.width, self.height), 255)
        self.draw_black = ImageDraw.Draw(self.black_img)
        self.draw_red = ImageDraw.Draw(self.red_img)


    def update_reading(self, value, direction):
        self.draw_black.rectangle(((20,30), (20,200)), fill = 255)
        if (direction in red_chars):
            self.draw_red.text((140, 20), direction, font = self.font60, fill = 0)
        else:
            self.draw_black.text((140, 20), direction, font = self.font60, fill = 0)
        if (value > 20 or value < 4):
            self.draw_red.text((30, 20), str(value), font = self.font60, fill = 0)
        else:
            self.draw_black.text((30, 20), str(value), font = self.font60, fill = 0)

    def update_graph(self, image):
        pass

    def draw(self):
        raise Exception("Shouldn't call base class draw")