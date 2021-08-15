#getting a dictionary from a text file
#Getting a dictionary from a CSV file
import  csv
with open('treeorderssubset.csv', mode='r') as infile:
    reader = csv.reader(infile)
   #1st Video - creating a dictionary - walk them through this. And introduce the idea of a Case Study
    treeOrders ={}

    for row in reader:
        key = row[0]

        if key in treeOrders:
            previousCount = int(treeOrders[key])
            total = previousCount + int(row[1])
            treeOrders[key] = total
        else:
            treeOrders[key] = row[1]

    infile.close()

for subdivision in treeOrders:
    print(subdivision,end=" ")
    print(treeOrders[subdivision])

print(treeOrders)
