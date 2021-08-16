#list of mixed format numbers
numbers = [7, 22, 4.5, 99.7, '3', '5']

#convert numbers to integers using expression
integers = (int(n) for n in numbers)


names_list = ['Adam','Anne','Barry','Brianne','Charlie','Cassandra','David','Dana']

#Converts names to uppercase
uppercase_names = (name.upper() for name in names_list)


# list of names
names_list = ['Adam','Anne','Barry','Brianne','Charlie','Cassandra','David','Dana']

# too long
# reverse_uppercase = (name[::-1] for name in (name.upper() for name in names_list))

# breaking it up
uppercase = (name.upper() for name in names_list)
reverse_uppercase = (name[::-1] for name in upper_case)
