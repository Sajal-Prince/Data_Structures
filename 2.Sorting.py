"""
In this we will learn about the different types of sorting present in python. The most widely learnt sorting methods for beginner are
1. Bubble Sort
2. Selection Sort
3. Insertion Sort
4. Merging sort (Not recommended for beginners but is widely asked during Interviews)
5. Quick Sort (Not recommended for beginners but is widely asked during Interviews)

The first three are easily to learn and Implement but is not the fastest way of sorting.
Among the above sorting methods the Quick sort is the fastest sorting method.
"""


# First we create a swapping function that will help us in swapping the elements from one index to other and vice versa.
def swap(input_list, index_a, index_b):
    temp = input_list[index_a]
    input_list[index_a] = input_list[index_b]
    input_list[index_b] = temp
    return input_list

# This is the code for selection sort. It only takes Input_List as parameter.
def selection_sort(input_list):
    for i in range(0,len(input_list)-1):
        for j in range(i, len(input_list)):
            if input_list[i] > input_list[j]:
                swap(input_list,i,j)
    return input_list

# This is the code for Bubble sort. It only takes Input_List as parameter.
def bubble_sort(input_list):
    for _ in range(len(input_list)):
        swapped = 0
        for i in range(len(input_list)-1):
            if input_list[i] > input_list[i+1]:
                swap(input_list, i, i+1)
                swapped = 1

        if swapped == 0:
            return input_list
    return input_list

# This is the code for Insertion sort. It only takes Input_List as parameter.
def insertion_sort(input_list):
    for i in range(1,len(input_list)):
        swapped = 0
        while i>0 and input_list[i] < input_list[i-1]:
            swap(input_list, i, i-1)
            i-=1
            swapped = 1
            if swapped ==0:
                break
    return input_list


# Below this line you can try to call the functions and check if the code is working or not.