class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return "Node object: data={}".format(self.data)

    def getData(self):
        """Return the self.data attribute."""
        return self.data

    def setData(self, new_data):
        """Replace the existing value of the self.data attribute with new_data
        parameter."""
        self.data = new_data

    def getNext(self):
        """Return the self.next attribute"""
        return self.next

    def setNext(self, new_next):
        """Replace the existing value of the self.next attribute with new_next
        parameter."""
        self.next = new_next

    def getPrevious(self):
        """Return the self.previous attribute"""
        return self.previous

    def setPrevious(self, new_previous):
        """Replace the existing value of the self.previous attribute with
        new_previous parameter."""
        self.previous = new_previous


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "Double Linked List object: head=".format(self.head)

    def isEmpty(self):
        return self.head is None

    def size(self):
        """Traverses the Linked List and returns an integer value representing
        the number of nodes in the Linked List.

        The time complexity is O(n) because every Node in the Linked List must
        be visited in order to calculate the size of the Linked List.
        """
        size = 0
        if self.head is None:
            return 0

        current = self.head
        while current is not None:  # While there are still Nodes left to count
            size += 1
            current = current.getNext()

        return size

    def search(self, data):
        """Traverses the Linked List and returns True if the data searched for
        is present in one of the Nodes. Otherwise, it returns False.

        The time complexity is O(n) because in the worst case, we have to visit
        every Node in the list.
        """
        if self.head is None:
            return "Linked List is empty. No Nodes to search."

        current = self.head
        while current is not None:
            if current.getData() == data:
                return True
            else:
                current = current.getNext()

        return False

    def addFront(self, new_data):
        """Add a Node whose data is the new_data argument to the front of the
        Linked List."""
        temp = DLLNode(new_data)
        temp.setNext(self.head)

        if self.head is not None:
            self.head.setPrevious(temp)

        self.head = temp

    def remove(self, data):
        """Removes the first occurence of a Node that contains the data argument
        as its self.data attribute. Returns nothing.

        The time complexity is O(n) because in the worst case, we have to visit
        every Node before finding the one we want to remove.
        """
        if self.head is None:
            return "Linked List is empty. No Nodes to remove."

        current = self.head
        found = False
        while not found:
            if current.getData() == data:
                found = True
            else:
                if current.getNext() is None:
                    return "A Node with that data value is not present."
                else:
                    current = current.getNext()

        if current.previous is None:
            self.head = current.getNext()
        else:
            current.previous.setNext(current.getNext())
            current.next.setPrevious(current.getPrevious())
