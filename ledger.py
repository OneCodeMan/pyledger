import csv

class Ledger:

	def __init__(self):
		self.entries = []
		self.total = 0.0

		# CSV stuff
		with open("myledger.txt", "w") as ledgerFile:
			ledgerFileWriter = csv.writer(ledgerFile)
			ledgerFileWriter.writerow(["ITEM", "PRICE"])

		ledgerFile.close()

	def add(self, item, price):
		
		# Slice item string if over 50 characters
		if (len(item) > 50): 
			item = item[:50]

		# Make price a float with 2 decimal places
		price = float(price)

		# Add price of item entered to total
		self.total += price

		# Add item and price to entries
		self.entries.append([item, price])

	def get_total(self):
		print(self.total)

	def get_entries(self):
		print(self.entries)



l = Ledger()