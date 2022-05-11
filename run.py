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
This works by checking adjacent items and swapping items in the list. 

Params:

array - one param of the array you would like to sort

"""
def bubble_sort(array):
    #get length of array passed into the function
    array_len = len(array)

    for i in range(array_len):
        #set flag so function can terminate early
        array_is_sorted = True

        #Loop that will run to sort items. Compares value with agjacent value
        for j in range(array_len - i - 1):
            #checks to see if first value is greater than adjacent value
            if array[j] > array[j + 1]:
                #swaps items if adjacent value is greater then item value [j]
                array[j], array[j + 1] = array[j + 1], array[j]
                array_is_sorted = False

        #if there are no swaps or array is sorted then break
        if array_is_sorted:
            break
    return array

"""
Description:

This is the insertion sort function. It will take an unorganised array and sorts the items from smallest to largest.
Passing items from unsorted list to the sorted list rearranging elements in approproate position.  

Params:

array - one param of the array you would like to sort

"""
def insertion_sort(array):
    #get length of array passed into the function
    array_len = len(array)

    for i in range(1, array_len):
        
        #define adjacent element value
        j = i-1

        nxt_element = array[i]
      
        #move elemements of array greater than next element to position of current
        while j >= 0 and nxt_element < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = nxt_element
    return array

def merge_sort(array):
    array_len = len(array)
    #This will break function if items in list are 1 or less
    if array_len <= 1:
        return array

    print("There is sorting to do")


# test = bubble_sort(array)
# print(test)

# test1 = insertion_sort(array)
# print(test1)

# test2 = merge_sort(array)
# print(test2)
