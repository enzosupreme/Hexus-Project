import time
import random
from mealtime import eatery
from film import moviebot
from board import SCL, SDA
import board
import busio
import digitalio
from digitalio import DigitalInOut, Direction, Pull
import terminalio
from adafruit_display_text import label
from adafruit_hid.keycode import Keycode
import adafruit_ssd1306

i2c = busio.I2C(SCL,SDA)

display =adafruit_ssd1306.SSD1306_I2C(128,64,i2c)

meal = eatery()
tv = moviebot()

a = DigitalInOut(board.A0)
a.direction = Direction.INPUT
a.pull = Pull.UP

b = DigitalInOut(board.A1)
b.direction = Direction.INPUT
b.pull = Pull.UP

c = DigitalInOut(board.A2)
c.direction = Direction.INPUT
c.pull = Pull.UP

d = DigitalInOut(board.A3)
d.direction = Direction.INPUT
d.pull = Pull.UP

x = 37
sx = str(x)
title = " Template"

x = 15
while True:
    display.text(title,x,6,1 )
    r = random.randint(0,2)
    display.show()

    if not a.value:
        display.fill(0)
        display.show()
        x = 45
        title = "A"

    if not b.value:
        display.fill(0)
        display.show()
        x = 45
        title = "B"


    if not c.value:
        display.fill(0)
        display.show()
        x = 45
        title = "C"
    if not d.value:
        display.fill(0)
        display.show()
        x = 45
        title = "D"





