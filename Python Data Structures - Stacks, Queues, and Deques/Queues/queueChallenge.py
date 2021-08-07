import random

class PrintQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if(len(self.items) > 0):
            return self.items.pop()

        return None

    def peek(self):
        if (len(self.items) > 0):
            return self.items[-1]

        return "The print queue is empty."

    def size(self):
        return ("The print queue has currently", len(self.items), "jobs in the queue.")

    def isEmpty(self):
        if (self.items == []):
            return "The print queue is empty."

        return "The print queue is not empty."

class Job:
    def __init__(self):
        self.pages = random.randrange(1, 11)

    def printPage(self):
        if (self.pages > 0):
            self.pages -= 1

    def checkComplete(self):
        if (self.pages > 0):
            return "The print job has not been completed."

        return "The print job was completed."

class Printer:
    def __init__(self):
        self.job = None

    def getJob(self, printQueue):
        try:
            self.job = printQueue.dequeue()
        except Exception:
            return "There are no jobs pending in the print queue."

    def print(self, job):
        while job.pages > 0:
            job.printPage()

        if job.checkComplete():
            return "Printing successful."
        else:
            return "An error occurred."

theJob = Job()
printQ = PrintQueue()
printer = Printer()

printQ.enqueue(theJob)
print(printQ.items)

printer.getJob(printQ)
print(printQ.items)
print(printer.print(printer.job))
