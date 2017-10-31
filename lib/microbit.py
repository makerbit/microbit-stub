# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


def panic():
    """
    Put micro:bit in panic() mode and display an unhappy face.
    Press the reset button to exit panic() mode.
    """
    pass


def sleep(time):
    """
    Put micro:bit to sleep for some milliseconds (1 second = 1000 ms) of time.
    sleep(2000) gives micro:bit a 2 second nap.
    """
    pass


def running_time():
    """
    Return running_time() in milliseconds since micro:bit's last reset.
    """
    pass


def temperature():
    """
    Return micro:bit's temperature in degrees Celcius.
    """
    pass


# Accelerometer 3D orientation
class _Accelerometer(object):
    def get_x(self):
        """
        Return micro:bit's tilt (X acceleration) in milli-g's.
        """
        pass

    def get_y(self):
        """
        Return micro:bit's tilt (Y acceleration) in milli-g's.
        """
        pass

    def get_z(self):
        """
        Return micro:bit's up-down motion (Z acceleration) in milli-g's.
        Z is a positive number when moving up. Moving down, Z is a negative
        number.
        """
        pass

    def is_gesture(self, name):
        """
        Return True or False to indicate if the named gesture is currently
        active.
        MicroPython understands the following gestures: 'up', 'down', 'left',
        'right', 'face up', 'face down', 'freefall', '3g', '6g', '8g' and
        'shake'.
        """
        pass

    def was_gesture(self, name):
        """
        Return True or False to indicate if the named gesture was active since
        the last call.
        MicroPython understands the following gestures: 'up', 'down', 'left',
        'right', 'face up', 'face down', 'freefall', '3g', '6g', '8g' and
        'shake'.
        """
        pass

    def get_gestures(self):
        """
        Return a list indicating the gesture history. The most recent gesture
        is last.
        Calling this method also clears the gesture history.
        MicroPython understands the following gestures: 'up', 'down', 'left',
        'right', 'face up', 'face down', 'freefall', '3g', '6g', '8g' and
        'shake'.
        """
        pass


accelerometer = _Accelerometer()


# Pushbutton
class _Button(object):
    def is_pressed(self):
        """
        If the button is pressed down, is_pressed() is True, else False.
        """
        pass

    def was_pressed(self):
        """
        Use was_pressed() to learn if the button was pressed since the last
        time was_pressed() was called. Returns True or False.
        """
        pass

    def get_presses(self):
        """
        Use get_presses() to get the running total of button presses, and also
        reset this counter to zero.
        """
        pass


button_a = _Button()
button_b = _Button()


# Compass 3D direction heading
class _Compass(object):
    def is_calibrated(self):
        """
        If micro:bit's compass is_calibrated() and adjusted for accuracy,
        return True.
        If compass hasn't been adjusted for accuracy, return False.
        """
        pass

    def calibrate(self):
        """
        If micro:bit is confused, calibrate() the compass to adjust the its
        accuracy.
        Will ask you to rotate the device to draw a circle on the display.
        Afterwards, micro:bit will know which way is north.
        """
        pass

    def clear_calibration(self):
        """
        Reset micro:bit's compass using clear_calibration() command.
        Run calibrate() to improve accuracy.
        """
        pass

    def get_x(self):
        """
        Return magnetic field detected along micro:bit's X axis.
        Usually, the compass returns the earth's magnetic field in micro-Tesla
        units.
        Unless...a strong magnet is nearby!
        """
        pass

    def get_y(self):
        """
        Return magnetic field detected along micro:bit's Y axis.
        Usually, the compass returns the earth's magnetic field in micro-Tesla
        units.
        Unless...a strong magnet is nearby!
        """
        pass

    def get_z(self):
        """
        Return magnetic field detected along micro:bit's Z axis.
        Usually, the compass returns the earth's magnetic field in micro-Tesla
        units.
        Unless...a strong magnet is nearby!
        """
        pass

    def get_field_strength(self):
        """
        Return strength of magnetic field around micro:bit.
        """
        pass

    def heading(self):
        """
        Return a number between 0-360 indicating the device's heading. 0 is
        north.
        """
        pass


compass = _Compass()


# Display 5x5 LED grid
class _Display(object):
    def show(self, x, delay=400, wait=True, loop=False, clear=False):
        """
        Use show(x) to print the string or image 'x' to the display. If 'x' is
        a list of images they will be animated together.
        Use 'delay' to specify the speed of frame changes in milliseconds.
        If wait is False animation will happen in the background while the
        program continues.
        If loop is True the animation will repeat forever.
        If clear is True the display will clear at the end of the animation.
        """
        pass

    def scroll(self, string, delay=150,
               wait=True, loop=False, monospace=False):
        """
        Use scroll(string) to scroll the string across the display.
        Use delay to control how fast the text scrolls.
        If wait is False the text will scroll in the background while the
        program continues.
        If loop is True the text will repeat forever.
        If monospace is True the characters will always take up 5
        pixel-columns.
        """
        pass

    def clear(self):
        """
        Use clear() to clear micro:bit's display.
        """
        pass

    def get_pixel(self, x, y):
        """
        Use get_pixel(x, y) to return the display's brightness at LED pixel
        (x,y).
        Brightness can be from 0 (LED is off) to 9 (maximum LED brightness).
        """
        pass

    def set_pixel(self, x, y, b):
        """
        Use set_pixel(x, y, b) to set the display at LED pixel (x,y) to
        brightness 'b'
        which can be set between 0 (off) to 9 (full brightness).
        """
        pass

    def on(self):
        """
        Use on() to turn on the display.
        """
        pass

    def off(self):
        """
        Use off() to turn off the display.
        """
        pass

    def is_on(self):
        """
        Use is_on() to query if the micro:bit's display is on (True) or off
        (False).
        """
        pass


display = _Display()


# Pins
class _Pin(object):
    """
    A standard pin
    """
    def read_digital(self):
        """
        Read the digital value of the pin. 0 for low, 1 for high
        """
        pass

    def write_digital(self, value):
        """
        Set the pin to output high if value is 1, or to low, it it is 0.
        """
        pass


class _AnaloguePin(_Pin):
    """
    These pins have ADC & PWM support
    """
    def read_analog(self):
        """
        Read the voltage applied to the pin.
        Returns the reading as a number between 0 (meaning 0v) and 1023
        (meaning 3.3v).
        """
        pass

    def write_analog(self, value):
        """
        Set the pin to output a value between 0 and 1023.
        """
        pass

    def set_analog_period(self, period):
        """
        Set the period of the PWM signal output to period milliseconds.
        """
        pass

    def set_analog_period_microseconds(self, period):
        """
        Set the period of the PWM signal output to period microseconds.
        """
        pass


class _GiantPin(_AnaloguePin):
    """
    These pins are aranged on the bottom of the board and have holes through
    them
    """
    def is_touched(self):
        """
        Returns if the pin is being physically touched on the hardware
        """
        pass


pin0 = _GiantPin()
pin1 = _GiantPin()
pin2 = _GiantPin()
pin3 = _AnaloguePin()
pin4 = _AnaloguePin()
pin5 = _Pin()
pin6 = _Pin()
pin7 = _Pin()
pin8 = _Pin()
pin9 = _Pin()
pin10 = _AnaloguePin()
pin11 = _Pin()
pin12 = _Pin()
pin13 = _Pin()
pin14 = _Pin()
pin15 = _Pin()
pin16 = _Pin()
# Pin17 = 3v3
# Pin18 = 3v3
pin19 = _Pin()
pin20 = _Pin()
# pin21 = gnd
# pin22 = gnd


# I2C
class _I2C(object):
    def read(self, address, n, repeat=False):
        """
        Use read(address, n) to read 'n' bytes from the device with the 7-bit
        address.
        If repeat is True, no stop bit will be sent.
        """
        pass

    def write(self, adress, buffer, repeat=False):
        """
        Use write(address, buffer) to write to the 'buffer' of the device at
        the 7-bit 'address'.
        If repeat is True, no stop bit will be sent.
        """
        pass

    def init(self, frequency, scl, sda):
        """
        Use init(frequency, scl, sda) to set the bus frequency and pins.
        """
        pass


i2c = _I2C()


# Image
class Image(object):
    def __init__(self, *args):
        """
        There are three ways to construct an image
        First, with a string:
            Image(
                '09090:'
                '99999:'
                '99999:'
                '09990:'
                '00900:'
            )
            This would create a 5x5 heart shaped image.
            Numbers go from 0 (off) to 9 (brightest).
            Note the colon ':' to set the end of a row. You can also use \\n
        Second with a width/height:
            Image(5, 5)
            This creates a blank 5x5 image, which you can manipulate
        Lastly you can pass a buffer with a width and a height
            Image(5, 5, [
                0, 9, 0, 9, 0,
                9, 9, 9, 9, 9,
                9, 9, 9, 9, 9,
                0, 9, 9, 9, 0,
                0, 0, 9, 0, 0,
            ])
            This would create the heart image from the first method.
        """

    def width(self):
        """
        Return the width of the image in pixels.
        """
        pass

    def height(self):
        """
        Return the height of the image in pixels.
        """
        pass

    def get_pixel(self, x, y):
        """
        Use get_pixel(x, y) to return the image's brightness at LED pixel
        (x,y).
        Brightness can be from 0 (LED is off) to 9 (maximum LED brightness).
        """
        pass

    def set_pixel(self, x, y, b):
        """
        Use set_pixel(x, y, b) to set the LED pixel (x,y) in the image to
        brightness 'b' which can be set between 0 (off) to 9 (full brightness).
        """
        pass

    def shift_left(self, n):
        """
        Use shift_left(n) to make a copy of the image but moved 'n' pixels to
        the left.
        """
        pass

    def shift_right(self, n):
        """
        Use shift_right(n) to make a copy of the image but moved 'n' pixels to
        the right.
        """
        pass

    def shift_up(self, n):
        """
        Use shift_up(n) to make a copy of the image but moved 'n' pixels up.
        """
        pass

    def shift_down(self, n):
        """
        Use shift_down(n) to make a copy of the image but moved 'n' pixels
        down.
        """
        pass

    def copy(self):
        """
        Use copy() to make a new exact copy of the image.
        """
        pass

    def crop(self, x1, y1, x2, y2):
        """
        Use crop(x1, y1, x2, y2) to make a cut-out copy of the image where
        coordinate (x1,y1) is the top left corner of the cut-out area and
        coordinate (x2,y2) is the bottom right corner.
        """
        pass

    def invert(self):
        """
        Use invert() to make a negative copy of the image. Where a pixel was
        bright or on in the original, it is dim or off in the negative copy.
        """
        pass


Image.HEART = Image()
Image.HEART_SMALL = Image()
Image.HAPPY = Image()
Image.SMILE = Image()
Image.SAD = Image()
Image.CONFUSED = Image()
Image.ANGRY = Image()
Image.ASLEEP = Image()
Image.SURPRISED = Image()
Image.SILLY = Image()
Image.FABULOUS = Image()
Image.MEH = Image()
Image.YES = Image()
Image.NO = Image()
Image.CLOCK12 = Image()
Image.CLOCK11 = Image()
Image.CLOCK10 = Image()
Image.CLOCK9 = Image()
Image.CLOCK8 = Image()
Image.CLOCK7 = Image()
Image.CLOCK6 = Image()
Image.CLOCK5 = Image()
Image.CLOCK4 = Image()
Image.CLOCK3 = Image()
Image.CLOCK2 = Image()
Image.CLOCK1 = Image()
Image.ARROW_N = Image()
Image.ARROW_NE = Image()
Image.ARROW_E = Image()
Image.ARROW_SE = Image()
Image.ARROW_S = Image()
Image.ARROW_SW = Image()
Image.ARROW_W = Image()
Image.ARROW_NW = Image()
Image.TRIANGLE = Image()
Image.TRIANGLE_LEFT = Image()
Image.CHESSBOARD = Image()
Image.DIAMOND = Image()
Image.DIAMOND_SMALL = Image()
Image.SQUARE = Image()
Image.SQUARE_SMALL = Image()
Image.RABBIT = Image()
Image.COW = Image()
Image.MUSIC_CROTCHET = Image()
Image.MUSIC_QUAVER = Image()
Image.MUSIC_QUAVERS = Image()
Image.PITCHFORK = Image()
Image.XMAS = Image()
Image.PACMAN = Image()
Image.TARGET = Image()
Image.TSHIRT = Image()
Image.ROLLERSKATE = Image()
Image.DUCK = Image()
Image.HOUSE = Image()
Image.TORTOISE = Image()
Image.BUTTERFLY = Image()
Image.STICKFIGURE = Image()
Image.GHOST = Image()
Image.SWORD = Image()
Image.GIRAFFE = Image()
Image.SKULL = Image()
Image.UMBRELLA = Image()
Image.SNAKE = Image()
Image.ALL_CLOCKS = Image()
Image.ALL_ARROWS = Image()


# uart
class _UARTSerial(object):
    def init(self, baudrate=9600, bits=8, parity=None,
             stop=1, tx=None, rx=None):
        """
        Use init() to set up communication using the default values.
        Otherwise override the defaults as named arguments.
        """
        pass

    def any(self):
        """
        If there are incoming characters waiting to be read, any() will return
        True.
        Otherwise, returns False.
        """
        pass

    def read(self, n):
        """
        Use read() to read characters.
        Use read(n) to read, at most, 'n' bytes of data.
        """
        pass

    def readall(self):
        """
        Use readall() to read as much data as possible.
        """
        pass

    def readline(self):
        """
        Use readline() to read a line that ends with a newline character.
        """
        pass

    def readinto(self, buf, n):
        """
        Use readinto(buf) to read bytes into the buffer 'buf'.
        Use readinto(buff, n) to read, at most, 'n' number of bytes into 'buf'.
        """
        pass

    def write(self, buf):
        """
        Use write(buf) to write the bytes in buffer 'buf' to the connected
        device.
        """
        pass


uart = _UARTSerial()


# SPI
class _SPISerial(object):
    def init(self, baudrate=1000000, bits=8, mode=0,
             sclk=pin13, mosi=pin15, miso=pin14):
        """
        Set up communication. Override the defaults for baudrate, mode,
        SCLK, MOSI and MISO. The default connections are pin13 for SCLK, pin15
        for MOSI and pin14 for MISO.
        """
        pass

    def write(self, buf):
        """
        Use write(buf) to write bytes in buffer 'buf' to the connected device.
        """
        pass

    def read(self, n):
        """
        Use read(n) to read 'n' bytes of data.
        """
        pass

    def write_readinto(self, outbuf, inbuf):
        """
        Use write_readinto(outbuf, inbuf) to write the 'outbuf' buffer to the
        connected device and read any response into the 'inbuf' buffer. The
        length of the buffers should be the same. The buffers can be the same
        object.
        """
        pass


spi = _SPISerial()