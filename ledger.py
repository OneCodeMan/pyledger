import csv
from tabulate import tabulate

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
			csv_entries = list(reader) # NESTED LIST OF ENTRIES
		f.close()

		# Gets rid of empty lists
		entries = [entry for entry in csv_entries if len(entry)]
		entries.append(["TOTAL", self._total])

		headers = ["ITEM", "PRICE ($)"]
		tablefmt = "grid"

		# Output in pretty form
		print(tabulate(entries, headers, tablefmt))

	def add(self, item, price):
		# Add total to price
		self._total += float(price)

		# Slice item string if too long
		if len(item) > 50:
			item = item[:49]

		# Add to csv
		with open(self._name, "a") as f:
			writer = csv.writer(f)
			writer.writerow([item, price])
		f.close()

	def get_total(self):
		print(self._total)