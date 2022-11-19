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
chest = Loot()
tv = moviebot()
lt = chest.item[0]



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
title = "  Micro-Chip\n\nA)LootBox\nB)Yes/No\nC)What to Watch?\nD)What to Eat?"

def movie_genre():
    r = random.randint(0,len(tv.genre) -1)
    return tv.genre[r]

def movie_decade():
    r = random.randint(0,len(tv.decade) -1)
    return tv.decade[r]

def noms():
    r = random.randint(0,len(meal.food) -1)
    return meal.food[r]

def items():
    roll = random.randint(0,len(chest.item)-1)

    return chest.item[roll]
def answers():
    answer = ["    Yes","Absolutely"," Of Course", "I think so","    Yep","   Nope","     No","Absolutely Not", "Probably Not", "   No way"]
    roller = random.randint(0,len(answer) -1)
    return answer[roller]


def roll(x):
    display.fill(0)
    display.show()
    r = random.randint(1,x)
    s = str(r)
    display.text(s,55,30,1)
    time.sleep(0.25)
    display.show()






x = 15
while True:
    display.text(title,x,6,1 )
    r = random.randint(0,2)
    display.show()

    if not a.value:

        if r is 0:
            title = items()
        if r is 1:
            title = arm()
        if r is 2:
            title = weaps()

        x = 10
        display.fill(0)
        display.show()
        time.sleep(0.025)
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
        display.text(g,40,30,1)
        display.show()
    if not d.value:
        display.fill(0)
        display.show()
        x = 15
        n = noms()
        title = "You should eat:"
        display.text(n,10,30,1)
        display.show()





