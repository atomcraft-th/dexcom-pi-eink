import os
import logging
from pi_display import PiDisplay

class PngDisplay(PiDisplay):
    def __init__(self) -> None:
        super().__init__(250, 122)
        self.image_num = 0

    def draw(self):
        filename = "image" + str(self.image_num) + ".png"
        self.black_img.save(filename)
        self.image_num = self.image_num + 1