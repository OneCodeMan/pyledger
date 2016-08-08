import csv

class Ledger:

	def __init__(self):
		self._total = 0.0
		self._name = "myledger.txt"

		with open(self._name, "w") as f:
			reader = csv.reader(f)

	def add(self, item, price):
		# Add to csv
		with open(self._name, "a") as f:
			writer = csv.writer(f)
			writer.writerow([item, price])
		# Add total to price
		# Slice item string if too long

	def display_ledger(self):
		pass
		# Read csv
		# Output in a list