# Swap all uppercase characters to lowercase and vice versa
def swapCases(strIn, flag):
    if(flag == 'upper'):
        print(strIn.upper())
    else:
        print(strIn.lower())

swapCases(input('Please enter the string to be swapped: '), input('upper/lower: '))