from random import randint
from microbit import *
# Microbit Dice 
# Version 1.0
# Display a random number in a dice format on
# the bbc microbit LED pixel grid
# Code ported from Pi Minecraft Rolldice.py

# A 5x5 layout of pixels for each dice face
# from our Pi Minecraft example
# The microbit has 9 levels of brightness
# Our dice will default to max brightness, hence "9"
six = "90009", "00000", "90009", "00000", "90009"
five = "90009", "00000", "00900", "00000", "90009"
four = "90009", "00000", "00000", "00000", "90009"
three = "90000", "00000", "00900", "00000", "00009"
two = "00000", "00900", "00000", "00900", "00000"
one = "00000", "00000", "00900", "00000", "00000"
dice = [one, two, three, four, five, six]


def drawDice(throw):
    # Could not get Image to work with array data, even after munging it.
    # Resorted to set_pixel
    display.clear()
    # Get the list of pixels for the number thrown
    bitmap = dice[throw]
    # Step through the 5 rows
    for y in range(0, 5):
        # Step through the columns
        for x in range(0, 5):
            pixel = int(bitmap[y][x])
            display.set_pixel(x, y, pixel)
    sleep(10)


def rollDice():
    # Animate between 7-16 throws before stopping
    # If the number chosen is the same as the previous one
    # don't count it as a throw and throw again
    # This makes it look like the dice is actually "rolling"
    display.clear()
    # For the first throw, we set the last_throw to a number 
    # outside of the range of valid throws, so it will be different
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

# Start here, chessboard is shown just to show we are starting up
display.show(Image.CHESSBOARD)
sleep(1000)
display.clear()

rollDice()
sleep(2000)

# We will loop forever and just wait for either button to be pressed
while True:
    if (button_a.is_pressed() or button_b.is_pressed()):
        rollDice() 
    sleep(1)        
