def addCal(num1, num2):
    return (f'ADDITION: {num1+num2}')

def subCal(num1, num2):
    return (f'SUBTRACTION: {num1-num2}')

def mulCal(num1, num2):
    return (f'MULTIPLICATION: {num1*num2}')

def divCal(num1, num2):
    return (f'DIVISION: {num1/num2}')

flag = False

# Check if the operation is STOP
while(flag == False):
    # Read the operation to be performed
    op = input('\nPlease enter the operation ADD/SUB/MUL/DIV/STOP ')
    if(op == 'STOP'):
        flag = True
    elif(op != 'ADD' and op != 'SUB' and op != 'MUL' and op != 'DIV'):
        print('\nPlease enter valid operation')
        continue
    else:
        # Read the input numbers
        num1,num2 = map(int, input('\nPlease enter two numbers for the operation ').split())

        try:
            if(op == 'ADD'):
                print(addCal(num1,num2))
            elif(op == 'SUB'):
                print(subCal(num1,num2))
            elif(op == 'MUL'):
                print(mulCal(num1,num2))
            elif(op == 'DIV'):
                print(divCal(num1,num2))
        except Exception as e:
            print(f'Exception caught - {e}. Invalid input!')




