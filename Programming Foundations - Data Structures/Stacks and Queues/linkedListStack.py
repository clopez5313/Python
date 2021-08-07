# Node class for the Linked List.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create the Stack class.
class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    # toString representation.
    def __str__(self):
        current = self.head.next
        output = ""

        while current:
            output += str(current.value)

            if(current.next != None):
                output += "->"

            current = current.next

        return output

    # Size of the stack.
    def getSize(self):
        return self.size

    # Checks if stack is empty.
    def isEmpty(self):
        return self.size == 0

    # Checks the top element of the stack.
    def peek(self):
        if(self.isEmpty()):
            raise Exception("The stack is empty.")
        return self.head.next.value

    # Adds an element to the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    # Removes the top element from the stack.
    def pop(self):
        if(self.isEmpty()):
            raise Exception("The stack is empty.")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1

        return remove.value

# Main method.
if __name__ == "__main__":
    stack = Stack()

    # Add data to the stack and print it.
    for i in range(0, 10):
        stack.push(i)
    print(f"Stack: {stack}")

    # Remove data, print each item removed, and print the final stack.
    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")
