class Deque:
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.insert(0, item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        if self.items:
            return self.items.pop(0)

        return None

    def removeRear(self):
        if self.items:
            return self.items.pop()

        return None

    def peekFront(self):
        if self.items:
            return self.items[0]

        return None

    def peekRear(self):
        if self.items:
            return self.items[-1]

        return None

    def size(self):
        return len(self.items)

    def isEmpty(self):
        if self.items:
            return "The deque is not empty."

        return "The deque is empty."

    def isPalindrome(self, word):
        self.items.clear()

        for letter in word:
            self.addRear(letter)

        while (self.size() > 1):
            frontLetter = self.removeFront()
            rearLetter = self.removeRear()

            if(frontLetter != rearLetter):
                return False

        return True

myDeque = Deque()
print(myDeque.isPalindrome("racecar"))
print(myDeque.isPalindrome("orange"))
