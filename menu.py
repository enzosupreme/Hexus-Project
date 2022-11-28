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

x = 45
sx = str(x)
title = " "
def left_eye():
    for i in range(10):
        display.pixel(i+20,30,1)
    for i in range(10):
        display.pixel(20,30+i,1)
    for i in range(10):
        display.pixel(i+20,40,1)
    for i in range(10):
        display.pixel(30,30+i,1)
def right_eye():
    for i in range(10):
        display.pixel(i+90,30,1)
    for i in range(10):
        display.pixel(90,30+i,1)
    for i in range(10):
        display.pixel(i+90,40,1)
    for i in range(10):
        display.pixel(100,30+i,1)
def eye(h,l):
    for i in range(60):
        display.pixel((i+h),l,i)
    for i in range(12):
        display.pixel(h,(l+i),1)
    for i in range(60):
        display.pixel((i+h),(l+12),1)
    for i in range(12):
        display.pixel((h+60),(l+i),1)


def wink():
    for i in range(10):
        display.pixel(i+20,30,1)
    for i in range(10):
        display.pixel(20,30+i,1)
    for i in range(10):
        display.pixel(i+20,40,1)
    for i in range(10):
        display.pixel(30,30+i,1)
    display.show()
    display.fill(0)
    display.show()
    for i in range(10):
        display.pixel(i+20,35,1)

x= 15
ex = 15
wy = 35
s = 5
r = 17
while True:
    display.fill(0)
    display.text(title,x,6,1 )
    display.text("D&D Tools",11,20,1)
    display.text("Dice Roller",71,20,1)
    display.text("Helper",11,40,1)
    display.text("Info",71,40,1)

    #for i in range(80):
        #display.pixel(20+i,55,1)
    #display.show()

    if s >65:
        s = 5
    if s < 4:
        s = 60
    if r > 37:
        r = 17
    if r < 16:
        r = 37
    while not d.value:
        if not a.value:
            print("pressed")
            display.fill(0)
            display.text("HELLO!",45,30,1)
            display.show()
    if not a.value:
        #ex-=10
        s-=60
    if not b.value:
        r-=20
    if not c.value:
        r+=20
    if not d.value:
        #ex+=10
        s+=60

    eye(s,r)
    display.show()




