# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

RATE_250KBIT = 250000
RATE_1MBIT = 1e+6
RATE_2MBIT = 2e+6


def on():
    """
    Turns on the radio. This needs to be called since the radio draws power
    and takes up memory that you may otherwise need.
    """
    pass


def off():
    """
    Turns off the radio, thus saving power and memory.
    """
    pass


def config(
    length=32,
    queue=3,
    channel=7,
    power=0,
    address=0x75626974,
    group=0,
    data_rate=RATE_1MBIT,
):
    """
    Configures the various settings relating to the radio.
    The specified default values are sensible.

    'length' is the maximum length, in bytes, of a message. It can be up to
             251 bytes long.
    'queue' is the number of messages to store on the message queue.
    'channel' (0-100) defines the channel to which the radio is tuned.
    'address' is an arbitrary 32-bit address that's used to filter packets.
    'group' is an 8-bit value used with 'address' when filtering packets.
    'data_rate' is the throughput speed. It can be one of:
                radio.RATE_250KBIT, radio.RATE_1MBIT (the default) or
                radio.2MBIT.
    """
    pass


def reset():
    """
    Reset the settings to their default value.
    """
    pass


def send_bytes(message):
    """
    Sends a message containing bytes.
    """
    pass


def receive_bytes():
    """
    Receive the next incoming message from the message queue.
    Returns 'None' if there are no pending messages.
    Messages are returned as bytes.
    """
    pass


def send(message):
    """
    Send a message string.
    """
    pass


def receive():
    """
    Receive the next incoming message from the message queue as a string.
    Returns 'None' if there are no pending messages.
    """
    pass
