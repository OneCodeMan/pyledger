import csv

class Ledger:

	def __init__(self):
		self._filename = "myledger.txt"
		self._entries = [["ITEM", "PRICE"]]
		self._total = 0.0

		# Create a CSV and add a starting row
		with open(self._filename, "w+") as ledgerFile:
			ledgerFileWriter = csv.writer(ledgerFile)
			ledgerFileWriter.writerow(self._entries)

		ledgerFile.close()

	def add(self, item, price):
		
		# Slice item string if over 50 characters
		if (len(item) > 50): 
			item = item[:50]

		# Make price a float with 2 decimal places
		price = float(price)

		# Add price of item entered to total
		self._total += price

		# Add item and price to entries
		self._entries.append([item, price])

		# Add the item and price to CSV
		with open(self._filename, "w") as ledgerFile:
			ledgerFileWriter = csv.writer(ledgerFile)
			ledgerFileWriter.writerows(self._entries)

		ledgerFile.close()

	def delete(self, item):
		# Do this if you can
		pass

	def get_total(self):
		print(self._total)

	def get_entries(self):
		print(self._entries)

	def display_ledger(self):
		with open(self._filename, 'r') as ledgerFile:
			reader = csv.reader(ledgerFile)
			self._entries = list(reader)
		print(self._entries)
		ledgerFile.close()
