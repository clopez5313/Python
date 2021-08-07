# Create a Queue class using Lists.
class Queue:
    def __init__(self):
        self.queue = list()

    # Add an element to the Queue.
    def addElement(self, value):
        if value not in self.queue:
            self.queue.insert(0, value)

            return True
        return False

    # Remove an element from the Queue.
    def removeElement(self):
        if(len(self.queue)>0):
            return self.queue.pop()
        return ("The queue is empty.")

    # Get the size of the Queue.
    def size(self):
        return len(self.queue)

theQueue = Queue()
theQueue.addElement("Apple")
theQueue.addElement("Mango")
theQueue.addElement("Guava")
theQueue.addElement("Papaya")

print("The length of the queue is:", theQueue.size())
print(theQueue.removeElement())
print(theQueue.removeElement())
