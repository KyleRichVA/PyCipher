'''
A simple Python Program which takes text or text file and converts it to
a 'sceret message' which can be converted back to a human readable text
Created by Kyle Richardson
'''

import shelve
import string
import random

# Set Character Lists for upper and lower case
LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase


def make_secret(text=None, filename=None):
    """make_secret: Converts either text or file to a secret code file"""
    # get a random value between 1 and 5 for the total steps.
    step = random.randint(1, 5)
    # make the step either negative or positive steps randomly
    direction = random.choice([-1, 1])
    step = step * direction
    # create a dictionary which aligns each char to it's secret version.
    cipher = stepdict(step)
    # set up code which determines the cipher
    code = step * 34 - 26 + 12
    # read the file if we have one
    if filename:
        txt = open(filename)
        text = txt.read()
        txt.close()
    secret_txt = ""
    # convert text to secret text
    for char in text:
        if char in LOWER or char in UPPER:
            secret_txt = secret_txt + cipher[char]
        else:
            secret_txt = secret_txt + char
    # save everything to a database
    message = shelve.open('secret_message')
    message['text'] = secret_txt
    message['code'] = code


def read_secret(filename):
    """read_secret: Takes a secret code file and converts it
    to human readable text"""
    # open up the file and get out the text and cipher code
    secret = shelve.open(filename)
    text = secret['text']
    code = secret['code']
    secret.close()
    # convert code to step
    step = int((code - 12 + 26) / 34)
    step = step * -1
    # create the cipher
    cipher = stepdict(step)
    read_text = ""
    # convert the secret text to readable text
    for char in text:
        if char in LOWER or char in UPPER:
            read_text = read_text + cipher[char]
        else:
            read_text = read_text + char
    # print out the text to the terimal
    print("YOUR SECRET MESSAGE:")
    print(read_text)


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
        index += 1
    index = 0
    for char in UPPER:
        newindex = index + step
        # loops around
        if (newindex > 25):
            newindex = newindex - 26
        if (newindex < 0):
            newindex = 26 + newindex
        cipher[char] = UPPER[newindex]
        index += 1
    return cipher


def menu():
    """Main Menu of the Program first thing that runs."""
    # testing
    make_secret(filename='sometext.txt')
    print("Now I'm gonna read it")
    read_secret('secret_message')


if __name__ == "__main__":
    menu()
