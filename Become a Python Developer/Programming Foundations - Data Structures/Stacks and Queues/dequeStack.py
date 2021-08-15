from collections import deque

# Create the structure.
stack = deque()

# Add elements and print the initial stack.
stack.append("a")
stack.append("b")
stack.append("c")

print("Initial stack:")
print(stack)

# Remove elements and print the final stack.
print("\nElements popped from stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("\nStack after elements were popped:")
print(stack)
