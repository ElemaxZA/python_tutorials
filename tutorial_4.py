# IF/ELIF/ELSE statements
# Python makes use of indentation NB!

# Syntax
# if condition == True:
    # do this

height = input('Input your height in metres?: ')

if int(height) <= 1:
    print("You cannot ride! Under 1m")
elif int(height) == 5:
    print("Wow you are so tall!")
elif int(height) >= 2:
    print("You are too tall! Over 2m")
else:
    print("You can ride!")