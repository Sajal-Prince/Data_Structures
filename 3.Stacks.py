"""
Stacks are Linear Data Structures that works on the principle of Last-In-First-Out bases.
Stacks have few methods that helps to manipulate the data in set. Let us see them one by one.

Stack have two main attributes:
1. Stack bottom always remains - 0
2. Stack top -  Always teels us the position of top element
3. Stack Size - Total number of data it can have
*(Basic knowledge of Classes in python are required)

1. Peek - returns the very top element
2. Insert - Insert the elements to top of the stack.
3. Pop - Remove the last inserted element.
4. IsEmpty - If the Stack Top is -1
5. IsFull - If the Stack Top is equal to the Size -1 of the stack.
"""

class Stack:
    def __init__(self,stack_size):
        self.stack = []
        self.stack_top = -1
        self.stack_size = stack_size

    def is_empty(self):
        if self.stack_top == -1:
            return True
        return False

    def is_full(self):
        if self.stack_top == self.stack_size - 1:
            return True
        return False

    def insert(self,element):
        if self.is_full():
            print("Stack Overflow State. Cannot be added. Please delete few element first.")
        else:
            self.stack_top += 1
            self.stack.append(element)
            print(f"{element} added to the stack")

    def peek(self):
        if self.is_empty():
            print("Stack is empty. No element to show")
        else:
            print(f"{self.stack[self.stack_top]} is the Top element")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow State. Cannot remove and Element. Please add few element first.")
        else:
            self.stack_top -= 1
            print(f"{self.stack.pop()} is removed from the stack")

    def display(self):
        print("stack : ",self.stack)

# You can now call teh class as an object and try to use the methods.