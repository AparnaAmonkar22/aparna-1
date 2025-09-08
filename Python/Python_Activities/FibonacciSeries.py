# Write a code in python which will give you a Fibonacci series to a number when you enter it

def fibonacci(num, range_num):
    fibList = list([num])
    print(fibList[0])
    
    if (num == 0):
        fibList.append(num+1)
        print(fibList[1])
    elif(num == 1):
        fibList.append(num)
        print(fibList[1])

    indx = 1
    for indx in range(1,range_num-1):
        fibList.append(fibList[indx]+fibList[indx-1])
        print(fibList[indx+1])


fibonacci(int(input('Please enter starting number for the series 0/1: ')), int(input('Please enter the range: ')))