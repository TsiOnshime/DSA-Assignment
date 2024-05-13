# Consider an array of integers in Java, named array, containing elements as
# follows: {3, 7, 1, 9, 4}. 
# Write a Java method named deleteElement that takes two parameters: the array and 
# an integer representing the index of the element to delete.
# The method should delete the element at the specified index from the array and return the modified array.
# If the index is invalid (less than 0 or greater than or equal to the array length),
# the method should print "Invalid index." and return the original array unchanged.


def delElement(arr,index):
    if index < 0 or index == len(arr):
        print("Invalid Index")
    new_arr = []
    for i in range (0, index):
        new_arr[i] = arr [i]
    for j in range (index, len(arr)-1):
        new_arr[i] = arr [i+1]
    return new_arr
print(delElement([2,3,4,6],1))