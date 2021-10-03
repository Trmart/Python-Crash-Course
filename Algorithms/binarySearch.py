#Taylor Martin
#10/2/21
#Algorithms in Python
#Iterative binary search algorithm in Python 3
# O(log) time 


def binarySearch(list, val): 
    first = 0 
    last = len(list) - 1 
    while(first <= last):
        mid = (first + last)/2
        if(list[mid]== val):
            return mid
        if(list[mid] > last):
            last = mid -1 
        else:
            first = mid +1
    return -1

