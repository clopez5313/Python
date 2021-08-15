# Create the structure. Add some data and print it.
queue = []

queue.append("a")
queue.append("b")
queue.append("c")

print("Initial queue:")
print(queue)

# Remove elements and print final queue.
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue) 
