'''generic display class to be used as the basis for additional displays'''
import os
from PIL import Image,ImageDraw,ImageFont

red_chars = ["↑↑", "↓↓", "?", "-"]

class PiDisplay:
    '''Generic display class'''
    def __init__(self, width, height) -> None:
        self.imgdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'img')
        self.reading_font = ImageFont.truetype(os.path.join(self.imgdir, 'Font.ttc'), 40)
        self.width = width
        self.height = height
        self.black_img = Image.new('1', (self.width, self.height), 255)
        self.red_img = Image.new('1', (self.width, self.height), 255)
        self.draw_black = ImageDraw.Draw(self.black_img)
        self.draw_red = ImageDraw.Draw(self.red_img)

        self.text_tl = (150, 20)
        self.text_br = (240, 55)
        self.arrow_tl = (150, 65)
        self.arrow_br = (240, 100)

    def update_reading(self, value, direction):
        self.draw_black.rectangle((self.text_tl, self.arrow_br), fill = 255)
        if (direction in red_chars):
            self.draw_red.text(self.arrow_tl, direction, font = self.reading_font, fill = 0)
        else:
            self.draw_black.text(self.arrow_tl, direction, font = self.reading_font, fill = 0)
        if (value > 20 or value < 4):
            self.draw_red.text(self.text_tl, str(value), font = self.reading_font, fill = 0)
        else:
            self.draw_black.text(self.text_tl, str(value), font = self.reading_font, fill = 0)

    def update_graph(self, glucose_readings):

        pass

    def draw(self):
        raise Exception("Shouldn't call base class draw")