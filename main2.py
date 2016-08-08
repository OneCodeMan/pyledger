import csv

with open("test2.txt", "r") as testFile:
	testFileReader = csv.reader(testFile)
	testList = []
	for row in testFileReader:
		if len(row) != 0:
			testList += [row]

testFile.close()

print(testList)

item = input("Enter item: ")
price = input("Enter price: ")

with open("test.txt", "a") as testFile:
	testFileWriter = csv.writer(testFile)
	testFileWriter.writerow([item, price])

testFile.close()

print(testList)