# Create some tuples.
tuple1 = ("Physics","Chemistry",1997,2000)
tuple2 = (1,2,3,4,5)
tuple3 = "a","b","c","d"
emptyTuple = ()

# Accessing values in tuples.
print("tuple1[0]:", tuple1[0])
print("tuple2[1:5]:", tuple2[1:5])

# Create a new tuple based on existing ones.
newTuple = tuple1 + tuple3
print(newTuple)
