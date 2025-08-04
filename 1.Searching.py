"""
In this we are going to learn about the algorith for implementation of searching. Searching are of two types mainly.
1. Liner search --> Where each element is checked with the required value and if the required value is present, we give output as True else we give output as false.
2. Binary Search --> This is more efficient way of searching for the elements. In this we check the middle index Element and if the key is smaller than the element then we simply delete the all the elements above the list hypothetically. And we keep doing the same otherwise. But the basic requirement is to have a sorted list.

Time Complexity -
a) Linear Search - O(N)
B) Binary Search - O(LogN)
"""

# Below is Implementation of Linear Search.
def linear_search(input_list, key):
    for i in input_list:
        if i == key:
            return True
    return False

# Below is the Implementation of Binary Search assuming that the list is Sorted.
def binary_search(sorted_input_list, key):

    low_index = 0
    high_index = len(sorted_input_list)

    while high_index >= low_index:
        mid = low_index + (high_index - low_index) // 2
        if sorted_input_list[mid] == key:
            return True
        elif sorted_input_list[mid] > key:
            high_index = mid-1
        else:
            low_index = mid+1
    return False


# Below this line you can call the functions and check for the output.