# Use mergesort to sort the numbers you entered in question 1.
from ExamQ1 import arr

def divide(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    mid = (len(arr)-1) // 2
    left = divide(arr[:mid])
    right = divide(arr[mid:])
    sort = merge (left,right)
    return sort
def merge (left, right):
    sorted_list = []
    i = 0
    j = 0
    while i < len (left) and j < len (right):
        if left [i] < right [j]:
           sorted_list.append (left [i])
           i += 1 
        else:
          sorted_list.append (right [j])
          j += 1
    sorted_list += right [j:] 
    sorted_list += left[i:]
    print(sorted_list) 
divide(arr)  
    
    