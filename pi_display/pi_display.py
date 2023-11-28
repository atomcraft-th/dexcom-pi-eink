'''generic display class to be used as the basis for additional displays'''
import os

class PiDisplay:
    '''Generic display class'''
    def __init__(self) -> None:
        self.imgdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'img')

    def update_reading(self, value, direction_char):
        pass

    def update_graph(self, image):
        pass