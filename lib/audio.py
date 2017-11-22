from __future__ import absolute_import, unicode_literals

from microbit import pin0, pin1


def play(source, wait=True, pins=(pin0, pin1)):
    """
    Play the source to completion where 'source' is an iterable, each element
    of which must be an AudioFrame instance.
    """
    pass


class AudioFrame(list):
    """
    Represents a list of 32 samples each of which is a signed byte.
    It takes just over 4ms to play a single frame.
    """
    pass
