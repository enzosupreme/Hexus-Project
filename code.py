import time
import random
import alarm
from mealtime import eatery
from film import moviebot
from board import SCL, SDA
import board
import busio
import digitalio
from lootbox import Loot
from fortune import cookie
from digitalio import DigitalInOut, Direction, Pull
import terminalio
from adafruit_display_text import label
from adafruit_hid.keycode import Keycode
import adafruit_ssd1306

i2c = busio.I2C(SCL,SDA)

display =adafruit_ssd1306.SSD1306_I2C(128,64,i2c)

meal = eatery()
tv = moviebot()
fc = cookie()
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
title = "Micro-Chip"
chest = Loot()
meal = eatery()



def noms():
    r = random.randint(0, len(meal.food) - 1)
    mf = meal.food[r]
    display.fill(0)
    display.text("You should eat:",15,1,1)
    display.text(mf,10,30,1)
def fortune_cookie():
    r = random.randint(0,len(fc.blessings) -1)
    fcr = fc.blessings[r]
    display.fill(0)
    display.text("Your Fortune:",35,1,1)
    display.text(fcr,5,17,1)
def roll(x):
    display.fill(0)
    display.show()
    r = random.randint(1,x)
    strx = ("D" + str(x))
    s = str(r)
    display.text(strx,55,1,1)
    display.text(s,55,30,1)
    display.show()
    time.sleep(0.5)
def answers():
    answer = ["    Yes","Absolutely"," Of Course", "I think so","    Yep","   Nope","     No","Absolutely Not", "Probably Not", "   No way"]
    roller = random.randint(0,len(answer) -1)
    ar = answer[roller]
    display.fill(0)
    display.text("The Answer IS:",20,1,1)
    display.text(ar,25,27,1)
    display.show()
    time.sleep(0.025)
def arm():
    roll = random.randint(0,len(chest.armor)-1)
    broll = random.randint(0,len(chest.buff)-1)
    sroll = random.randint(0,len(chest.stats)-1)
    rol = random.randint(5, 250)
    ro = random.randint(1,10)
    r = random.randint(2,15)

    a = str(chest.armor[roll])
    b = str(chest.buff[broll])
    c = str(ro)
    d = str(chest.stats[sroll])
    sr = str(r)
    srol = str(rol)
    full_arm = (f'{a} \n\n+{c} {d}\n{b} Resistance\nWeight:  Value:\n{sr} lbs    {srol}GP')

    display.text(full_arm,10,1,1)
    display.show()

def weaps():
    broll = random.randint(0,len(chest.buff)-1)
    wroll = random.randint(0,len(chest.weapon)-1)
    droll = random.randint(0,len(chest.dice)-1)
    num = random.randint(1,10)
    rol = random.randint(5, 250)
    r = random.randint(2,15)

    b = str(chest.buff[broll])
    die = str(chest.dice[droll])
    w = str(chest.weapon[wroll])
    snum = str(num)
    sd = str(droll)
    srol = str(rol)
    sr = str(r)

    weap_roll = (f'{w}\n\nDamage: +{snum}{die}\nSpecial:{b}\nWeight:  Value:\n{sr} lbs    {srol}GP')
    display.text(weap_roll,15,1,1)
    display.show()

def items():
    roll = random.randint(0,len(chest.item)-1)
    ci = chest.item[roll]
    display.text(ci,10,1,1)
    display.show()

def moviebot():
    rg = random.randint(0,len(tv.genre) -1)
    rd = random.randint(0,len(tv.decade) - 1)

    gen = tv.genre[rg]
    dec = tv.decade[rd]

    display.fill(0)
    display.text("You should watch a: ",15,1,1)
    display.text(dec,50,30,1)
    display.text(gen,25,40,1)
    display.show()

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
def box(h,l):
    for i in range(10):
        display.pixel((i+h),l,i)
    for i in range(12):
        display.pixel(h,(l+i),1)
    for i in range(10):
        display.pixel((i+h),(l+12),1)
    for i in range(12):
        display.pixel((h+10),(l+i),1)

def hi_light(h,l):
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
        display.pixel(i+20,25,1)
    for i in range(10):
        display.pixel(20,25+i,1)
    for i in range(10):
        display.pixel(i+20,35,1)
    for i in range(10):
        display.pixel(30,25+i,1)
    display.show()
    display.fill(0)
    display.show()
    for i in range(10):
        display.pixel(i+20,35,1)

def hell():
    for i in range(128):
        display.fill(0)
        display.text("Hello!",i,30,1)
        display.show()

def rain():
    r = random.randint(0,128)
    for i in range(0,60,20):
        display.fill(0)
        box(r,i)
        display.show()

def text_rain(word):
    r = random.randint(0,128)
    for i in range(0,60,20):
        display.fill(0)
        display.text(word,r,i,1)
        display.show()
def cbl_rain():
    oi = 15
    j = 7
    for i in range(5):
        text_rain(circa[(random.randint(0,13))])
        text_rain(circa[(random.randint(0,13))])
        text_rain(circa[(random.randint(0,13))])
        text_rain(circa[(random.randint(0,13))])
        text_rain(circa[(random.randint(0,13))])
    display.fill(0)
    for o in range(len(circa)):
        oi+=5
        #display.fill(0)
        for i in range(1,40,20):

            display.text(circa[o],oi,j+23,1)
        display.show()

def luck_buff():
    r = random.randint(1,100)
    sr = str(r) +" Luck"
    display.fill(0)
    display.text("Luck Buff",30,1,1)
    display.text("Good Luck!",30,17,1)
    display.text("You receive:",25,27,1)
    display.text("+",35,47,1)
    display.text(sr,40,47,1)



def default(horz,vertz):
    x = 30
    title = "Micro-Chip"
    display.fill(0)
    display.text(title,x,6,1 )
    display.text("LootBox",11,20,1)
    display.text("Dice",11,30,1)
    display.text("Answer",11,40,1)
    display.text("Food",11,50,1)
    display.text("Movie",81,20,1)
    display.text("Fortune",81,30,1)
    display.text("Luck",81,40,1)
    display.text("Demo",81,50,1)
    hi_light(horz,vertz)

cbl = [
    "circuit",
    "bored",
    "lab"
    ]
alfa = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",
    "t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","!","@",
    "#","$","%","^","&","*"
       ]

circa = [
    "c","i","r","c","u","i","t"," b"," o"," r"," e"," d","  l","  a","  b"
       ]

apps = [
    "fullproto",
    "microchip",
    "Template"
    ]
ex = 15
wy = 35
s = 5
r = 17
select = 1
default(s,r)
while True:
    ra = False
    rollin = random.randint(0,2)
    if (s == 5 and r == 17):
        select = 1
    if (s == 5 and r == 27):
        select = 2
    if (s == 5 and r == 37):
        select = 3
    if (s == 5 and r == 47):
        select = 4
    if(s == 70 and r == 17):
        select = 5
    if(s == 70 and r == 27):
        select = 6
    if(s == 70 and r == 37):
        select = 7
    if(s == 70 and r == 47):
        select = 8

    if s >71:
        s = 5
    if s < 5:
        s = 47
    if r > 47 and s == 5:
        r = 17
        s = 70
        default(s,r)
    if r > 47 and s == 70:
        r = 17
        s = 5
        default(s,r)
    if r < 16 and s == 5:
        s = 70
        r = 47
        default(s,r)
    if r < 16 and s == 70:
        s = 5
        r = 47
        default(s,r)

    while not a.value and not b.value:
        cbl_rain()
        #__import__("/apps/" + apps[1])

    if not a.value:
        r-=10
        default(s,r)
    if not b.value:
        r+=10
        default(s,r)
    if not c.value:
        s = 5
        r = 17
        default(s,r)
    if not d.value:
        if select is 1:
            if rollin is 0:
                display.fill(0)
                items()
                display.show()
                time.sleep(0.025)
            if rollin is 1:
                display.fill(0)
                arm()
                display.show()
                time.sleep(0.025)
            if rollin is 2:
                display.fill(0)
                weaps()
                display.show()
                time.sleep(0.025)

            time.sleep(0.025)
            display.show()
        if select is 2:
            roll(4)
            display.show()
            time.sleep(0.025)
        if select is 3:
            answers()
        if select is 4:
            noms()
        if select is 5:
            moviebot()
        if select is 6:
            fortune_cookie()
        if select is 7:
            luck_buff()
        if select is 8:
            i2c.unlock()
            __import__("/apps/" + apps[1])

    print(s)
    print(r)
    #print("Starting ", apps[0])
    #__import__("/apps/" + apps[1])
    display.show()




