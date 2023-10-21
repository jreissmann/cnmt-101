import random

# the number of times user rolls dice, decided by user input
dice_rolls = int(input ("How many times do you want to roll?"))

# the number of sides on the dice, decided by user input
dice_sides = int(input ("How many sides is your dice? [1-20]"))

# dice sides should be a positive number and between 1-20
if dice_sides <= 0 or dice_sides > 20:
    print("Please pick a positive number between 1-20")
    quit()
# the number of dice rolls should be greater than 0
elif dice_rolls <= 0:
    print("The amount of dice rolls should be greater than 0")
    quit()

# print statement for initializing rolls
print ("Rolling a", dice_sides, "sided die", dice_rolls, "times")

# for loop for dice rolls being rolled number of dice_rolls 
for rolls in range (dice_rolls):
    # make a variable for a randomly generated number within range of user input for dice sides
    randomDice = random.randint(1, dice_sides)
    # print the number generated
    print (randomDice)
    # if the random number generated is lowest number, user should just alt+f4
    if randomDice == 1:
        print ('JUST ALT+F4')
    # else if the random number generated being the highest dice side user specified then its a crit
    elif randomDice == dice_sides:
        print ('CRITICAL HIT!')

# once for loop is done, print finished rolling
print ('Finished rolling')
