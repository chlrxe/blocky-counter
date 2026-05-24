import valid as v
from valid import get_integer, get_y_or_n, get_string

#*******************************************************************************
# Author: chlrxe
# Created: 04/26/2026
# Last Updated: 5/24/26
#
# Description: This helps calculate how many blocks are necessary to create a
# hollow cubic home without a floor and user input amount to account for a door.
# This is for a blocky game like Minecraft or Vintage Story.
# in this assignment i add while conditions and iteration to main()
#
# Input: block name, length, width, height, door
#
# Output: total amount of blocks needed
#
# Dependencies: valid.py
#*******************************************************************************

# Sample Run

# Welcome to Block Counter!
# This tool can help you know how many blocks you need in order to
# create a hollow cubic structure w/out a floor and with or w/out a door.
# for games like Minecraft and Vintage Story!

# Enter block name: stone brick
# Enter length: 5
# Enter width: 5
# Enter height: 4

# Do you want a door? (y/n):
# Please enter yes or no.
# Do you want a door? (y/n): y
# How many blocks is your door? (Press Enter for 2):
# Door set to 2 blocks
# __________________________________________________

# To build this structure you will need:

# 1 stack(s) of 64, and 7 of stone brick

# Would you like to calculate again? (y/n): YES
# Enter block name: cobblestone
# Enter length: 7
# Enter width: 5
# Enter height: 5

# Do you want a door? (y/n): y
# How many blocks is your door? (Press Enter for 2): 4
# Door set to 4 blocks
# __________________________________________________

# To build this structure you will need:

# 1 stack(s) of 64, and 49 of cobblestone

# Would you like to calculate again? (y/n): n

# Goodbye!

# (Press enter to exit...)

def main():

    # variables
    block_name = ""
    long = 0
    wide = 0
    high = 0
    total_blocks = 0

    welcome_print()

    start = "y" # by default on at start until user says "n"

    while start in ["y", "yes"]:
        # inputs
        block_name = get_name()
        long = get_long()
        wide = get_wide()
        high = get_high()

        # calculations
        side_1_2 = calc_side_1_2(long, high)
        side_3_4 = calc_side_3_4(wide, high)
        side_5_6 = calc_side_5_6(long, wide)
        total_blocks = calc_total_blocks(side_1_2, side_3_4, side_5_6)

        # print of calculations
        calc_print(total_blocks, block_name, long, wide, high)

        # breaks loop if user inputs "n"
        start = v.get_y_or_n("\nWould you like to calculate again? (y/n): ")
        if start in ["n", "no"]:
            print("\nGoodbye!")
            input("\n(Press enter to exit...)")
            break

####### DEFINITIONS #######

def welcome_print():
    """
    Introduction
    """
    print("Welcome to Block Counter!\n")
    print("This tool can help you know how many blocks you need in order to\n")
    print("create a hollow cubic structure w/out a floor and with or w/out a door.\n")
    print("for games like Minecraft and Vintage Story!\n")

##### user inputs #####

def get_name():
    """
    Gets user input for block name
    :return: block_name (string)
    """
    block_name = ""
    block_name = v.get_string("\nEnter block name: ")
    return block_name

def get_long():
    """
    Gets user input for length
    :return: long (int)
    """
    while True:

        long = v.get_integer("Enter length: ")

        if long > 0:
            return long
        else:
            print("Error: Length must be greater than 0. Try again.")

def get_wide():
    """
    Gets user input for width
    :return: wide (int)
    """
    while True:
        wide = v.get_integer("Enter width: ")

        if wide >= 0:
            return wide
        else:
            print("Error: Width must be greater than 0. Try again.")


def get_high():
    """
    Gets user input for height
    :return: high (int)
    """
    while True:

        high = v.get_integer("Enter height: ")
        if high >= 0:
            return high
        else:
            print("Error: Height must be greater than 0. Try again.")

##### calculations #####

def calc_side_1_2(long, high):
    """
    This first part calculates sides 1 & 2 of the cubic structure
    :param long: length (int)
    :param high: height (int)
    :return: calc_side_1_2 (int)
    """
    calc_side_1_2 = 2 * (long * high)
    return calc_side_1_2

def calc_side_3_4(wide, high):
    """
    This second part calculates sides 3 & 4 of the cubic structure
    :param wide: width (int)
    :param high: height (int)
    :return: calc_side_3_4 (int)
    """
    side_3_4 = 2 * ((wide - 1) * (high - 1))
    return side_3_4

def calc_side_5_6(long, wide):
    """
    This third part calculates sides 5 & 6 of the cubic structure
    :param long: length (int)
    :param wide: width (int)
    :return: calc_side_5_6 (int)
    """
    side_5_6 = (long - 2) * (wide - 2)
    return side_5_6

def calc_total_blocks(side_1_2, side_3_4, side_5_6):
    """
    This final calculation calculates the amount of blocks you need
    in order to build the cubic structure
    :param side_1_2: side_1_2 (int)
    :param side_3_4: side_3_4 (int)
    :param side_5_6: side_5_6 (int)
    :return: total_blocks (int)
    """
    door_yn = ""
    door_yn = get_y_or_n("\nDo you want a door? (y/n): ")

    while door_yn not in ["y", "yes", "no", "n"]:
        print("Please enter either 'y' or 'n': ")
        door_yn = v.get_y_or_n("\nDo you want a door? (y/n): ")

    door = 0
    door_blocks = 0
    if door_yn in ["y", "yes"]:
        door_blocks = v.get_integer("How many blocks is your door?: ")
        door = door_blocks
        print("Door set to", door, "blocks")
    else:
        print("Ok, no door counted.")

    total_blocks = side_1_2 + side_3_4 + side_5_6 - door
    return total_blocks

def calc_print(total_blocks, block_name, long, wide, high):
    """
    End message
    :param total_blocks: total of blocks
    :param block_name: block name (string)
    :param long: length (int)
    :param wide: width (int)
    :param high: height (int)
    :return: Total number of blocks w/ info on stack amounts if applicable
    """
    STACK_SIZE = 64
    full_stacks = 0
    remainder_blocks = 0

    print("__________________________________________________")

    if total_blocks <= STACK_SIZE:
        print("\nTo build this structure you will need:\n")
        print(total_blocks, block_name)

    elif total_blocks > STACK_SIZE:
        full_stacks = total_blocks // STACK_SIZE
        remainder_blocks = total_blocks % STACK_SIZE
        print("\nTo build this structure you will need:\n")
        print(full_stacks, "stack(s) of 64, and", remainder_blocks, "of", block_name)

main()