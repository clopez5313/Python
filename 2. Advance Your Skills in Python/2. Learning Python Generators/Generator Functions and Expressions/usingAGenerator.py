# generator solution
def even_integers_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

# Manual calls.
integers = even_integers_generator(10)
# print(next(integers))
# print(next(integers))
# print(next(integers))

# Using a for loop.
for i in integers:
    print(i)
