# from numpy import random
import random

# Function to generate random number
def generateRandomNum(start, end):
    randNum = random.randint(start, end)
    print(f'Random Number: {randNum}')
    return randNum

attempts = 5
flag = False
start, end = map(int, input(f'Please enter the range for random number \"separated by space\" ').split())
num = generateRandomNum(start, end)
inp = int(input(f'Guess the number between {start} and {end} '))

# Loop in till 5 attempts
while (attempts !=  0):
    # Check if the number entered is within the range
    if(inp < start or inp > end):
        inp = int(input(f'\nInvalid number. \nPlease enter number between {start} and {end} '))
        continue #Recheck

    # If the number entered by user matches the random number
    # End the loop
    # Else continue the attempts
    if (inp == num):
        flag = True
        break
    else:
        attempts -= 1
        if(attempts == 0): break
        inp = int(input(f'\nSorry :(  \nYou have {attempts} attempts left.\nPlease try again '))

# Print the result
if flag == True:
    print('\nCONGRATULATIONS! YOU WON!!')
else:
    print(f'\nSORRY :( YOU LOST!!\nCorrect number was {num}')