from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Example usage
q = Queue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)

print("Dequeue:", q.dequeue())
print("Dequeue:", q.dequeue())
print("Is empty:", q.is_empty())
print("Size:", q.size())

#################################


import queue

# Create a new queue
q = queue.Queue()

# Enqueue elements
q.put(5)
q.put(10)
q.put(15)

# Dequeue elements
item1 = q.get()
item2 = q.get()

print("Dequeue:", item1)
print("Dequeue:", item2)
print("Is empty:", q.empty())
print("Size:", q.qsize())

