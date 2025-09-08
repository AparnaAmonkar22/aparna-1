'''
Write a code in python in which you can get “Fizz Buzz” 
for all numbers which can be divided by (3, 5, 15). 
The range should from (1 to 100).
'''
    
num=1

for num in range(1,100):
    # Use mod operator to find Fizz Buzz number
    
    if (num%3 == 0 and num%5 == 0):
        print(f'{num}: Fizz Buzz')
    elif(num%3 == 0):
        print(f'{num}: Fizz ')
    elif ( num%5 == 0):
        print(f'{num}: Buzz')