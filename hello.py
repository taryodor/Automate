#This program says hello and asks for my name

print("Hello world!")
print("What is your name?") #Asks for your name
myName = input()
print("It is nice to mmet you, ", myName)
print("The length of your name is: ", len(myName))
myAge = input("WHat is your age? ")
print("You will be {} in a year".format(str(int(myAge) + 1)))
