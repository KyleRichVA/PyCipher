'''
A simple Python Program which takes text or text file and converts it to
a 'sceret message' which can be converted back to a human readable text
Created by Kyle Richardson
'''

import os
import shelve
import string
import random

# Set Character Lists for upper and lower case
LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase


def make_secret(text=None, file=None):
    """make_secret: Converts either text or file to a secret code file"""
    # get a random value between 1 and 5 for the total steps.
    step = random.randint(1, 5)
    # make the step either negative or positive steps randomly
    direction = random.choice([-1, 1])
    step = step * direction
    # create a dictionary which aligns each char to it's secret version.
    cipher = stepdict(step)


def read_secret(file):
    """read_secret: Takes a secret code file and converts it
    to human readable text"""
    pass


def stepdict(step):
    """takes a step and creates a dictonary converting each char based off equation
    """
    index = 0
    cipher = {}
    # goes through all possible characters and converts them to a secret char
    # based off the step.
    for char in LOWER:
        newindex = index + step
        # loops around
        if (newindex > 25):
            newindex = newindex - 26
        if (newindex < 0):
            newindex = 26 + newindex
        cipher[char] = LOWER[newindex]
    for char in UPPER:
        newindex = index + step
        # loops around
        if (newindex > 25):
            newindex = newindex - 26
        if (newindex < 0):
            newindex = 26 + newindex
        cipher[char] = UPPER[newindex]
    return cipher


def codedict(code):
    """takes a code anf converts each char based off equation"""

def menu():
    """Main Menu of the Program first thing that runs."""
    pass

if __name__ == "__main__":
    menu()