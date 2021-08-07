# Create the object and add some elements.
pQueue = []

pQueue.append((2, "Apple"))
pQueue.append((1, "Mango"))
pQueue.append((3, "Banana"))

# Re-sort every time after a new element is inserted.
pQueue.sort(reverse=True)

while pQueue:
    nextItem = pQueue.pop()
    print(nextItem)
