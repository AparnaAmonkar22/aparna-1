# Swap the numbers with and without the 3rd Variable

# Using 3rd Variable
def swapNumWithVar(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp

    print(f'\nAfter Swapping With 3rd variable\nNum1 = {num1} and Num2 = {num2}\n')


# WihtOut using 3rd Variable
def swapNumWithOutVar(num1, num2):
    num1, num2 = num2, num1

    print(f'\nAfter Swapping withOut 3rd variable\nNum1 = {num1} and Num2 = {num2}\n')


# Using List
def swapTwoNumUsingList(num1, num2):
    listNum = list([num1, num2])
    listNum.reverse()

    print(f'\nAfter Swapping two numbers using List\nNum1 = {listNum[0]} and Num2 = {listNum[1]}\n')


num1 = int(input('Please enter Num1: '))
num2 = int(input('Please enter Num2: '))

print(f'\nBefore Swapping\nNum1 = {num1} and Num2 = {num2}\n')

# Using 3rd Variable
swapNumWithVar(num1, num2)

# WihtOut using 3rd Variable
swapNumWithOutVar(num1, num2)

# Using List
swapTwoNumUsingList(num1, num2)
