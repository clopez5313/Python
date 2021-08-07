from queue import Queue

# Create the Queue, check its size, and some elements, and check whether the queue is full.
myQueue = Queue(maxsize=3)

print(myQueue.qsize())

myQueue.put("a")
myQueue.put("b")
myQueue.put("c")

print("\nIs it full?:", myQueue.full())

# Remove some elements from the Queue, check if it's empty, add a new element, and finally check if the Queue is empty and full.
print("\nElements dequeued from the Queue:")
print(myQueue.get())
print(myQueue.get())
print(myQueue.get())

print("\nIs it empty?:", myQueue.empty())

myQueue.put(1)

print("\nIs it empty?:", myQueue.empty())
print("Is it full?:", myQueue.full())
