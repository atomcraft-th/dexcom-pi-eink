import os
import logging
from pi_display import PiDisplay

class PngDisplay(PiDisplay):
    def __init__(self) -> None:
        super().__init__(250, 122)
        self.image_num = 0

    def draw(self):
        logging.info("drawing")
        filename = "image" + str(self.image_num) + ".png"
        logging.info("writing " + filename)
        self.black_img.save(filename)
        self.image_num = self.image_num + 1
        self.reset_image()