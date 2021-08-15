class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "Linked List object: head={}".format(self.head)

    def isEmpty(self):
        """Returns True if the Linked List is empty. Otherwise, returns False."""
        return self.head is None  # self.head == None

    def addFront(self, new_data):
        """Add a Node whose data is the new_data argument to the front of the
        Linked List."""
        temp = Node(new_data)
        temp.setNext(self.head)
        self.head = temp

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

    def remove(self, data):
        """Removes the first occurence of a Node that contains the data argument
        as its self.data variable. Returns nothing.

        The time complexity is O(n) because in the worst case we have to visit
        every Node before we find the one we need to remove.
        """
        if self.head is None:
            return "Linked List is empty. No Nodes to remove."

        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == data:
                found = True
            else:
                if current.getNext() == None:
                    return "A Node with that data value is not present."
                else:
                    previous = current
                    current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
