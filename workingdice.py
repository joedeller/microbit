from random import randint
from microbit import *

six = "90009", "00000", "90009", "00000", "90009"
five = "90009", "00000", "00900", "00000", "90009"
four = "90009", "00000", "00000", "00000", "90009"
three = "90000", "00000", "00900", "00000", "00009"
two = "00000", "00900", "00000", "00900", "00000"
one = "00000", "00000", "00900", "00000", "00000"
dice = [one, two, three, four, five, six]


def drawDice(throw):
    display.clear()
    bitmap = dice[throw]
    for y in range(0, 5):
        for x in range(0, 5):
            pixel = int(bitmap[y][x])
            display.set_pixel(x, y, pixel)
    sleep(10)


def rollDice():
    display.clear()
    last_throw = 7
    rolls = 0
    max_rolls = randint(7,16)
    while rolls < max_rolls:
        throw = randint(0, 5)
        if throw != last_throw:
            drawDice(throw)
            sleep(200)
            last_throw = throw
            rolls = rolls + 1

display.show(Image.CHESSBOARD)
sleep(1000)
display.clear()

rollDice()
sleep(2000)

while True:
    if (button_a.is_pressed() or button_b.is_pressed()):
        rollDice() 
    sleep(1)        
