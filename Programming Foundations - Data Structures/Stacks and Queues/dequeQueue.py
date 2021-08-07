from collections import deque

# Create the object, add elements to the Queue and print it.
queue = deque()

queue.append("a")
queue.append("b")
queue.append("c")

print("Initial queue:")
print(queue)

# Remove elements from the Queue, and print it.
print("\nElements dequeued from the queue:")
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print("\nQueue after removing the elements:")
print(queue)
