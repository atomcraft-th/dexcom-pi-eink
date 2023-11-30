import os
import logging
from pi_display import PiDisplay

class PngDisplay(PiDisplay):
    def __init__(self) -> None:
        super().__init__(250, 122)

    def draw(self):
        self.black_img.save("image.png")