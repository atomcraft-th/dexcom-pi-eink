'''generic display class to be used as the basis for additional displays'''
import os
from PIL import Image,ImageDraw,ImageFont
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import logging

red_chars = ["↑↑", "↓↓", "-"]
ignore_chars = ["?"]

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
        self.graph_width = 165
        self.text_tl = (self.graph_width, 20)
        self.text_br = (240, 55)
        self.arrow_tl = (self.graph_width + 10, 65)
        self.arrow_br = (240, 100)

    def reset_image(self):
        self.black_img = Image.new('1', (self.width, self.height), 255)
        self.red_img = Image.new('1', (self.width, self.height), 255)
        self.draw_black = ImageDraw.Draw(self.black_img)
        self.draw_red = ImageDraw.Draw(self.red_img)

    def update_reading(self, value, direction):
        if (direction in red_chars):
            self.draw_red.text(self.arrow_tl, direction, font = self.reading_font, fill = 0)
        elif not (direction in ignore_chars):
            self.draw_black.text(self.arrow_tl, direction, font = self.reading_font, fill = 0)
        if (value > 20 or value < 4):
            self.draw_red.text(self.text_tl, str(value), font = self.reading_font, fill = 0)
        else:
            self.draw_black.text(self.text_tl, str(value), font = self.reading_font, fill = 0)

    def update_graph(self, glucose_readings):
        x = []
        y = []
        for reading in glucose_readings:
            x.append(reading.datetime)
            y.append(reading.mmol_l)
        y_max = max(y)
        y_max = max(y_max, 20)
        x_min = min(x)
        x_max = max(x)

        plt.xticks(fontsize=5)
        plt.figure(figsize=(self.graph_width / 100, self.height / 100))
        plt.plot(x, y, color='black', linewidth = 0,
                marker='.', markerfacecolor='black', markersize=3)

        # setting x and y axis range
        plt.ylim(0,y_max)
        plt.xlim(x_min,x_max)

        logging.info("x_max " + str(x_max))

        # naming the y axis
        #plt.ylabel('mmol / l')
        # plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        plt.gca().xaxis.set_visible(False)
        #plt.gca().yaxis..set_fontsize('xx-small')
        plt.gcf().subplots_adjust(left=0.15)
        canvas = plt.get_current_fig_manager().canvas
        canvas.draw()

        rgb_graph = Image.frombytes('RGB', canvas.get_width_height(), canvas.tostring_rgb())
        self.black_img.paste(rgb_graph.convert('1'), (10,0))

    def draw(self):
        raise Exception("Shouldn't call base class draw")
