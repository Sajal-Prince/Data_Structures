"""
Queues are Linear Data Structures that works on the principle of First-In-First-Out bases.
Queues have few methods that helps to manipulate the data. Let us see them one by one.

Queues have few main attributes:
1. Queue front always stores front element index
2. Queue rear always stores the rear most element mostly 0 in almost all cases.
3. Queue Size Total number of data it can have
*(Basic knowledge of Classes in python are required)

1. Enqueue - Insert the elements to top of the Queue.
3. Dequeue - Remove the last inserted element.
4. IsEmpty - If the Queue front is less than Queue rear
5. IsFull - If the Queue front is equal to the Size -1 of the Queue.
"""

class Queue:
    def __init__(self,queue_size):
        self.queue = []
        self.queue_front = -1
        self.queue_rear = 0
        self.size = queue_size

    def is_empty(self):
        if self.queue_front == -1:
            return True
        return False

    def is_full(self):
        if self.queue_front == self.size - 1:
            return True
        return False

    def enqueue(self,element):
        if self.is_full():
            print("Queue Overflow State. Cannot be added. Please delete few element first.")
        else:
            self.queue_front += 1
            self.queue.insert(self.queue_rear,element)
            print(f"{element} added to the queue")

    def peek_front(self):
        if self.is_empty():
            print("Queue is empty. No element to show")
        else:
            print(f"{self.queue[self.queue_front]} is the Front element")

    def peek_rear(self):
        if self.is_empty():
            print("Queue is empty. No element to show")
        else:
            print(f"{self.queue[self.queue_rear]} is the Rear element")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow State. Cannot remove and Element. Please add few element first.")
        else:
            self.queue_front -= 1
            print(f"{self.queue.pop()} is removed from the Queue")

    def display(self):
        print("Queue : ",self.queue)

# You can now call teh class as an object and try to use the methods.