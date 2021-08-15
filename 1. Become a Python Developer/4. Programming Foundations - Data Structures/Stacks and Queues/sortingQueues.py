import queue

# Create the object and add some elements to it.
myQueue = queue.Queue()

myQueue.put(14)
myQueue.put(27)
myQueue.put(11)
myQueue.put(4)
myQueue.put(1)

# Sort with Bubble Sort algorithm.
size = myQueue.qsize()

for i in range(size):
    # Remove the element.
    item = myQueue.get()

    #Remove the next element.
    for j in range(size-1):
        nextItem = myQueue.get()

        # Check which item is greater and put the smaller one at the beginning of the Queue.
        if item > nextItem:
            myQueue.put(nextItem)
        else:
            myQueue.put(item)
            item = nextItem
    myQueue.put(item)

while(myQueue.empty() == False):
    print(myQueue.queue[0], end=" ")
    myQueue.get()
