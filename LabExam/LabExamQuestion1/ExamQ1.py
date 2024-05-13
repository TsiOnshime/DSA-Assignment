# Write a program that allows the user to enter a sequence of numbers into an
# array. The program should then prompt the user to enter a number to be
# searched. The program should determine if the number is present in the array
# and, if so, display the number of times it appears.


def check(arr,element):
    count = 0 
    for i in range(len(arr)):
        if arr[i]== element:
            count+=1
            
        else:
            continue
    return count
arr= [1,3,5,1,6,7]
element= 1
print(check(arr,element))