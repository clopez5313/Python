# Node class
class Node:

	# Function to initialize the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize
						# next as null

# Linked List class
class LinkedList:

	# Function to initialize the Linked
	# List object
     def __init__(self):
          self.head = None

     # Function to print the elements of the Linked List.
     def printList(self):
          theNode = self.head

          while(theNode):
               print(theNode.data, end=" ")
               theNode = theNode.next

# Create a Linked List and add elements to it.
if __name__=='__main__':

    # Start with the empty list
    myList = LinkedList()

    myList.head = Node(1)
    second = Node(2)
    third = Node(3)

    '''
    Three nodes have been created.
    We have references to these three blocks as head,
    second and third

    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  | None |     | 2  | None |     |  3 | None |
    +----+------+     +----+------+     +----+------+
    '''

    myList.head.next = second; # Link first node with second

    '''
    Now next of first Node refers to second.  So they
    both are linked.

    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  | null |     |  3 | null |
    +----+------+     +----+------+     +----+------+
    '''

    second.next = third; # Link second node with the third node

    '''
    Now next of second Node refers to third.  So all three
    nodes are linked.

    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  |  o-------->|  3 | null |
    +----+------+     +----+------+     +----+------+
    '''
    myList.printList()
