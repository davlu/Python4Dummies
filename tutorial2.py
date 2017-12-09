#Hello fellow students, welcome to tutorial 2 where we will learn inputs, if, elif, else and equations signs in Python, buckle up for this lesson and let's go
#Let's do the same tactics from last tutorial, import the neccessary modules

import sys
import os
import math
import time

#Now this time we will create a string but a little bit different, this string is an input, the input is inputted by the user and gives us a output depending on the users answer to the question
#Let's try a basic one like what is 2 times 2 follow the code below!

#equation is the name of our string and input("") is out input, the parantheses is so you can write the question! I like to add str(input("")) to identify it as a string so there aren't errors but you can also do integers or don't type anything just input("")
equation = str(input("What is 2x2? "))

#Next we will use if and else statements for the answer, first we will use if for the correct answer, follow the code below!
if equation == ("2"):
	print("Correct answer! Congrats!")
	

#Now else if the answer is wrong!
else:
	quit("Invalid input!")

#return is the code to terminate the code

#Now let's try something different by using elif and the equations signs +, - and * (you can use / to divide but I don't like divisions sooo :v)

equation2 = str(input("Do you like math? Answer with y/n\n"))
#\n is to break a line but this won't affect the answer as it is!
if equation2 == ("y"):
	print("Pi rocks! " + 0 / 0)
	quit()
#I know I said no division but we got to do something to break the software hahah :3

#elif is the same as if, you just change the output
elif equation2 == ("n"):
	print(":v I hope you'll one day love this magnificient art!")
	quit()
else:
	print("Don't you dare try to break the code you greedy bastard, math will now punish you!")
	quit("Invalid input!")

#Learn to perfect elif, if and else by doing this simple exercise of trying to create a password system, when done submit this to Tally so he can grade and show your mistakes and perfection so we can all move on to while loops, hardest shit to learn :v