#Taylor Martin
#10/2/21
#Algorithms in Python
#Iterative binary search algorithm in Python 3
# O(log) time 


def binarySearch(arr, val): 
    first = 0 
    last = len(arr) - 1 
    while(first <= last):
        mid = (first + last)/2
        if(arr[mid]== val):
            return mid
        if(arr[mid] > last):
            last = mid -1 
        else:
            first = mid +1
    return -1

#recursive binary search 

def recursiveBinarySearch(arr, low, high, val): 
    #check recursive base case 
    if(high >= low):

        mid = (low+high)/ 2 
        #if the element is present at mid
        if(arr[mid] == val):
            return mid
        if(arr[mid] > val):
            return recursiveBinarySearch(arr, low, high -1, val) #recursive call to binary search function, high -1 
        if(arr[mid] < val):
            return recursiveBinarySearch(arr, low +1, high, val)
    else:
        return -1 