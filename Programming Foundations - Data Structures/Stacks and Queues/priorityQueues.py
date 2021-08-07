from queue import PriorityQueue

# Create object, add some items and print the items.
pQueue = PriorityQueue()

pQueue.put((2, "Apple"))
pQueue.put((1, "Banana"))
pQueue.put((3, "Mango"))

while not pQueue.empty():
    nextItem = pQueue.get()
    print(nextItem)
