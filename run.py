"""
This project looks to create algortihms to sort an array and to 
present user with visualrepresentation while doing so.

Algorithms to be introduced:
1. Bubble Sort
2. Insertion Sort
3. Merge Sort
4. Quicksort
5. Timsort

"""
import random

#This is random generated list between 1 and 10 that will be used for testing purposes.
array = [random.randint(1, 10) for i in range(10)]
print(array)

"""
Description:

This is the bubble sort function. It will take an unorganised array and sort items from smallest to largest. 

Params:

array - one param of the array you would like to sort

"""
def bubble_sort(array):
    #get length of array passed into the function
    n = len(array)

    for i in range(n):
        #set flag so function can terminate early
        array_is_sorted = True

        #Loop that will run to sort items. Compares value with agjacent value
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                #swaps items if adjacent value is greater then item
                array[j], array[j +1] = array[j + 1], array[j]
                array_is_sorted = False

        #if there are no swaps or array is sorted then break
        if array_is_sorted:
            break
    return array

test = bubble_sort(array)

print(test)
