# Function for Binary Search using recursive call
def BinarySearchAlgorithm(array, search, low, high):
    flag = False
    # low = 0
    # high = len-1

    # while(flag==False):
    if(low == high and search == array[low]):
        print(f'{search} found at {low} position successfully')
        # flag = True

    else:
        indx = int((low+high)/2)
        if(array[indx] == search):
            print(f'{search} found at {indx} position successfully')
            # flag = True

        elif(search > array[indx]):
            low = indx+1
            BinarySearchAlgorithm(array, search, low, high)
            # continue
        else:
            high = indx-1
            BinarySearchAlgorithm(array, search, low, high)
            # continue


# Search Array
searchArr = [1,2,3,5,7,8,9]
# Take the serach element 
searchEle = int(input('Enter search element from [1,2,3,5,7,8,9]: '))

# Call Binary Search functio 
# result = BinarySearchAlgorithm(searchArr, searchEle, len(searchArr))
result = BinarySearchAlgorithm(searchArr, searchEle, 0, len(searchArr)-1)