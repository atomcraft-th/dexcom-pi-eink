'''generic display class to be used as the basis for additional displays'''

class PiDisplay:
    '''Generic display class'''
    def update_reading(self, value, direction_char):
        pass

    def update_graph(self, image):
        pass