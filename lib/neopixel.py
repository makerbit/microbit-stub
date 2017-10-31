# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class NeoPixel(list):
    def __init__(self, pin, n):
        """
        Create a list representing a strip of 'n' neopixels controlled from
        the specified pin (e.g. microbit.pin0).
        Use the resulting object to change each pixel by position (starting
        from 0).
        Individual pixels are given RGB (red, green, blue) values between
        0-255 as a tupe.
        For example, (255, 255, 255) is white:

            np = neopixel.NeoPixel(microbit.pin0, 8)
            np[0] = (255, 0, 128)
            np.show()
        """
        pass

    def clear(self):
        """
        Clear all the pixels.
        """
        pass

    def show(self):
        """
        Show the pixels. Must be called for any updates to become visible.
        """
        pass
