# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from microbit import pin0


def set_tempo(number, bpm):
    """
    Make a beat last a 'number' of ticks long and played at 'bpm' beats per
    minute.
    """
    pass


def pitch(freq, length=-1, pin=pin0, wait=True):
    """
    Make micro:bit play a note at 'freq' frequency for 'length' milliseconds.
    E.g. pitch(440, 1000) will play concert 'A' for 1 second.
    If length is a negative number the pitch is played continuously.
    Use the optional pin argument to override the default output for the
    speaker.
    If wait is False the music will play in the background while the program
    continues.
    """
    pass


def play(music, pin=pin0, wait=True, loop=False):
    """
    Make micro:bit play 'music' list of notes. Try out the built in music to
    see how it works. E.g. music.play(music.PUNCHLINE).
    Use the optional pin argument to override the default output for the
    speaker.
    If wait is False the music will play in the background while the program
    continues.
    If loop is True, the tune will repeat.
    """
    pass


def get_tempo():
    """
    Return the number of ticks in a beat and number of beats per minute.
    """
    pass


def stop(pin=pin0):
    """
    Stops all music playback on the given pin.
    If no pin is given, pin0 is assumed.
    """
    pass


def reset():
    """
    If things go wrong, reset() the music to its default settings.
    """
    pass
