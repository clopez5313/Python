from fs.osfs import OSFS

totalSize = 0

# Open the directory and iterate over it. Check for .txt files only. Obtain their size and add it to the variable.
with OSFS(".") as fileSystem:
    for path in fileSystem.walk.files(filter=["*.txt"]):
        info = fileSystem.getinfo(path, namespaces=["details"])
        totalSize += info.size

# Print the total value.
print("Total size of files is: {0}".format(totalSize))
