# Hello fellow students, welcome to tutorial 2 where we will learn inputs, if, elif, else and equations signs in Python, buckle up for this lesson and let's go

# Now this time we will create a variable but a little bit different, this variable is an input, the input is inputted by the user and gives us a output depending on the users answer to the question
# Let's try a basic one like what is 2 times 2 follow the code below!

# equation is the name of our variable and input("") is our input, the parantheses is so you can write the question! I like to add that str(input("")) to identify it as a string so there aren't errors but you can also do integers or don't type anything just use input("")
# Input pretty much makes so you can fill a variable with information and store that just like a variable, the str() or int() is used so no thing other than string or no other thing than integer can be typed out into the input, using the if command the variable becomes a condition and if the input is the condition met with if it will output something
equation = str(input("What is 2x2? "))

# Next we will use if and else statements for the answer, first we will use if for the correct answer
# If is a command used in Python to recognize when a condition is met, when the condition is met the command will output the answer accordingly, for this example I'll use a simple print function but the output can be many other things
if equation == ("2"):
	print("Correct answer! Congrats!")
	
# Use else for when the condition is not met but instead something else is found in the variable, if the condition is not met or an invalid input is typed out the program outputs the following because no condition was met when searching the variable
else:
	quit("Invalid input!")

# quit() is a function in Python used to terminate a script, inside the () you can put arguments (Will be taught in tutorial5.py) and for now you just type "Invalid input!" in it when using else

# Now let's try something different by using elif and the equations signs +, - and * (you can use / to divide but I don't like divisions sooo :v)

equation2 = str(input("Do you like math? Answer with y/n\n"))
# \n is to break a line but this won't affect the answer as it is, \n will merely make it a new line for the user to input something into the variable
if equation2 == ("y"):
	print("Pi rocks! " + 0 / 0)
	quit()

# Elif is used when a command doesn't want to interfer with if, elif is used when a different set of condition is met in this case: n, if n is the condition met elif does the same as if and outputs the according answer
elif equation2 == ("n"):
	print(":v I hope you'll one day love this magnificient art!")
	quit()
else:
	print("Don't you dare try to break the code you greedy bastard, math will now punish you!")
	quit("Invalid input!")
