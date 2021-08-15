from queue import LifoQueue

# Create the structure.
stack = LifoQueue(maxsize=3)

# Print the number of elements in the stack.
print(stack.qsize())

# Add elements to the stack and check if the stack is full, and the size of the stack as well.
stack.put("a")
stack.put("b")
stack.put("c")

print("Is it full?:", stack.full())
print("Size:", stack.qsize())

# Remove elements from the stack and check whether it is empty at the end.
print("\nElements popped from the stack:")
print(stack.get())
print(stack.get())
print(stack.get())

print("Is it empty?:", stack.empty())
