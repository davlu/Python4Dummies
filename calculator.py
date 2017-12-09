#Author: Tatsuki
#The purpose of this script is to teach definitions and equations with Python
#Python version being used is Python 3.6.4

#Importing the necessarry modules and libraries for the script to work
import os
import sys
import math
import string

#Numbers to calculate
x = int(input('Insert the first number here: '))
y = int(input('Insert the second number here: '))

#Definitions for the equations:
def addition(x ,y):
	print('{} + {} Equals to:'.format(x, y))
	print(x + y)

def subtraction(x ,y):
	print('{} - {} Equals to:'.format(x, y))
	print(x - y)

def division(x ,y):
	print('{} / {} Equals to:'.format(x, y))
	print(x / y)

def multiplication(x ,y):
	print('{} * {} Equals to:'.format(x, y))
	print(x * y)

def percentage(x, y):
	print('The percentage of {} to {}:'.format(x, y))
	z = x / y
	print(z * 100)	

#Input for the type of equation to be done
equation_type = str(input('''
	Please type the type of equation you want,
	Traditional equations:
	multiplication
	division
	addition
	subtraction
	Misc equations:
	Getting a percentage: percentage
	'''))

#Used to determine what kind of operation should be done
if equation_type == ('addition'):
	addition(x, y)

elif equation_type == ('subtraction'):
	subtraction(x, y)

elif equation_type == ('division'):
	division(x, y)

elif equation_type == ('multiplication'):
	multiplication(x, y)

elif equation_type == ('percentage'):
	percentage(x, y)

#Error, if invalid input the system will quit and create a report log
else:
	sys.exit("Err: Input wasn't recognized by the code... please retry..")

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
if __name__ == "__main__":
    answer = raw_input("Do you want to restart this program ? ")
    if answer.lower().strip() in "y yes".split():