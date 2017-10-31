# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


def translate(words):
    """
    Return a string containing the phonemes for the English words in the
    string 'words'.
    """
    pass


def say(words, pitch=64, speed=72, mouth=128, throat=128):
    """
    Say the English words in the string 'words'.
    Override the optional pitch, speed, mouth and throat settings to change
    the tone of voice.
    """
    pass


def pronounce(phonemes, pitch=64, speed=72, mouth=128, throat=128):
    """
    Pronounce the phonemes in the string 'phonemes'.
    Override the optional pitch, speed, mouth and throat settings to change
    the tone of voice.
    """
    pass


def sing(song, pitch=64, speed=72, mouth=128, throat=128):
    """
    Sing the phonemes in the string 'song'.
    Add pitch information to a phoneme with a hash followed by a number
    between 1-255 like this: '#112DOWWWWWWWW'.
    Override the optional pitch, speed, mouth and throat settings to change
    the tone of voice.
    """
    pass
