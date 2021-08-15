class HashTable:
    def __init__(self, size):
        self.size = size
        self.hashTable = self.createBuckets()

    def createBuckets(self):
        return [[] for _ in range(self.size)]

    # Insert values into the table.
    def setValue(self, key, value):
        # Get the index from the key using the hash function.
        hashedKey = hash(key) % self.size

        # Get the bucket corresponding to the index.
        bucket = self.hashTable[hashedKey]
        found = False

        for index, record in enumerate(bucket):
            recordKey, recordValue = record

            # Check if the bucket has the same key as the key to be inserted.
            if recordKey == key:
                found = True
                break

        # If the bucket has the same key as the key to be inserted, update the key value. Otherwise, append the new key-value pair
        # to the bucket.
        if found:
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))

    # Return the searched value with a specific key.
    def getValue(self, key):
        # Get the index from the key using the hash function.
        hashedKey = hash(key) % self.size

        # Get the bucket corresponding to the index.
        bucket = self.hashTable[hashedKey]
        found = False

        for index, record in enumerate(bucket):
            recordKey, recordValue = record

            # Check if the bucket has the same key as the key being searched.
            if recordKey == key:
                found = True
                break

        # If the bucket has the same key as the key being searched, return the found value.
        # Otherwise, return that no record was found.
        if found:
            return recordValue
        else:
            return "No record found."

    # Remove a value with a specific key.
    def deleteValue(self, key):
        # Get the index from the key using the hash function.
        hashedKey = hash(key) % self.size

        # Get the bucket corresponding to the index.
        bucket = self.hashTable[hashedKey]
        found = False

        for index, record in enumerate(bucket):
            recordKey, recordValue = record

            # Check if the bucket has the same key as the key to be deleted.
            if recordKey == key:
                found = True
                break

        if found:
            bucket.pop(index)
        return

    # ToString method.
    def __str__(self):
        return "".join(str(item) for item in self.hashTable)

hTable = HashTable(50)

# Insert some values and print the data.
hTable.setValue("example@gmail.com", "Some value")
hTable.setValue("example@yahoo.com", "Another value")

print(hTable)
print()

# Search for a record using a key.
print(hTable.getValue("example@yahoo.com"))
print()

# Delete a value from the table.
hTable.deleteValue("example@yahoo.com")
print(hTable)
