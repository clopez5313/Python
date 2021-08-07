import heapq

# Create and initialize a List. Then convert it to a Heap with heapify.
myHeap = [21,1,45,78,3,5]

heapq.heapify(myHeap)
print(myHeap)

# Add an element to the Heap.
# heapq.heappush(myHeap, 8)
# print(myHeap)

# Remove an element from the Heap.
# heapq.heappop(myHeap)
# print(myHeap)

# Replace an element in the Heap.
heapq.heapreplace(myHeap, 6)
print(myHeap)
