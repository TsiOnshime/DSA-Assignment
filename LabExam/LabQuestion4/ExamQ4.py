#Implement the bubble sort algorithm to 
# sort an array of alphabets (ASCII).

def BubbleSortOnAlpha(arr):
    for i in range (len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j] 
    return arr
print(BubbleSortOnAlpha(['A','C']))
    