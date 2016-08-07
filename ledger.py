import csv

with open("test.txt", "r") as testFile:
	testFileReader = csv.reader(testFile)
	testList = []
	for row in testFileReader:
		if len(row) != 0:
			testList += [row]

testFile.close()

print(testList)