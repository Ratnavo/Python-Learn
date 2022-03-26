# write a function to find the smallest element in an array | Practicing from book

def findsmallest(arr):
    smallest = arr[0] #stores the smallest value
    smallest_index = 0   #stores the index of the smallest value
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
        return smallest_index

#using this above function to now write a selection sort algorithm

def selectionSort(arr):
    newArr = []
    for i in range (len(arr)):
        smallest = findsmallest(arr) # find the smallest element in the array, and adds it to the new array.
        newArr.append(arr.pop(smallest))
    return newArr

print :selectionSort([5,3,2,10])
