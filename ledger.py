import csv

class Ledger:

	def __init__(self):
		self._total = 0.0
		self._name = "myledger.txt"

		# Create csv
		with open(self._name, "w") as f:
			reader = csv.reader(f)
		f.close()

	def display_ledger(self):
		# Read csv
		with open(self._name, 'r') as f:
			reader = csv.reader(f)
			as_list = list(reader)
		f.close()

		# Output in a list
		print(as_list)

	def add(self, item, price):
		# Add total to price
		self._total += price

		# Slice item string if too long
		if len(item) > 50:
			item = item[:49]
			
		# Add to csv
		with open(self._name, "a") as f:
			writer = csv.writer(f)
			writer.writerow([item, price])
		f.close()