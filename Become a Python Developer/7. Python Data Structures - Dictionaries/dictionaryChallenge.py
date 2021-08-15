#getting a dictionary from a text file
#Getting a dictionary from a CSV file
import  csv
with open('treeorderssubsetnodupes.csv', mode='r') as infile:
    reader = csv.reader(infile)
   #creating a dictionary - walk through code.
   # And introduce the idea of a Case Study
    mydict ={}

    for row in reader:
        key = row[0]
        mydict[key]=row[1]

    infile.close()

print("The size of the dictionary is of", len(mydict), "elements.")
mydict['196'] = 2
print("The subdivision 196 now has", mydict['196'], "trees.")
mydict['999'] = 3
print("The new subdivision 999 has", mydict['999'], "trees.")

for item in mydict:
    print(item,end=" ")
    print(mydict[item])
