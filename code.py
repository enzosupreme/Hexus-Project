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

x = 1
sx = str(x)
title = "  Micro-Chip\n\nA)Dice\nB)Yes/No\nC)What to Watch?\nD)What to Eat?"

def movie_genre():
    r = random.randint(0,len(tv.genre) -1)
    return tv.genre[r]

def movie_decade():
    r = random.randint(0,len(tv.decade) -1)
    return tv.decade[r]

def noms():
    r = random.randint(0,len(meal.food) -1)
    return meal.food[r]

    return chest.item[roll]
def answers():
    answer = ["     Yes","  Absolutely","  Of Course", " I think so","     Yep","    Nope","     No","Absolutely Not", " Probably Not", "   No way"]
    roller = random.randint(0,len(answer) -1)
    return answer[roller]


def roll(x):
    display.fill(0)
    display.show()
    r = random.randint(1,x)
    s = str(r)
    return s

x = 15
while True:
    display.text(title,x,6,1 )
    r = random.randint(0,2)
    display.show()

    if not a.value:
        x = 55
        title = "DICE"
        d4 = roll(4)
        d6 = roll(6)
        d8 = roll(8)
        d10 = roll(10)
        d12 = roll(12)
        d20 = roll (20)
        display.text("D4",20,17,1)
        display.text("D6",60,17,1)
        display.text("D8",100,17,1)
        display.text("D10",20,40,1)
        display.text("D12",60,40,1)
        display.text("D20",100,40,1)
        display.text(d4,20,25,1)
        display.text(d6,60,25,1)
        display.text(d8,100,25,1)
        display.text(d10,20,50,1)
        display.text(d12,60,50,1)
        display.text(d20,100,50,1)
        display.show()

    if not b.value:
        x = 45
        display.fill(0)
        display.show()
        title = "Answer"
        ans = answers()
        display.text(ans,25,27,1)
        display.show()


    if not c.value:
        display.fill(0)
        display.show()
        x = 5
        g = movie_genre()
        dec = movie_decade()
        title = "You should watch a:"
        display.text(dec,50,20,1)
        display.text(g,22,30,1)
        display.show()

    if not d.value:
        display.fill(0)
        display.show()
        x = 15
        n = noms()
        title = "You should eat:"
        display.text(n,10,30,1)
        display.show()





