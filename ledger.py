"""
//
//                       _oo0oo_
//                      o8888888o
//                      88" . "88
//                      (| -_- |)
//                      0\  =  /0
//                    ___/`---'\___
//                  .' \\|     |// '.
//                 / \\|||  :  |||// \
//                / _||||| -:- |||||- \
//               |   | \\\  -  /// |   |
//               | \_|  ''\---/''  |_/ |
//               \  .-\__  '-'  ___/-. /
//             ___'. .'  /--.--\  `. .'___
//          ."" '<  `.___\_<|>_/___.' >' "".
//         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
//         \  \ `_.   \_ __\ /__ _/   .-` /  /
//     =====`-.____`.___ \_____/___.-`___.-'=====
//                       `=---='
//
//
//     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//     Code Buddha blesses this code to be bug free.
//
"""
import csv
import re
import glob
from tabulate import tabulate

class Ledger:

	def __init__(self):
		self._total = 0.0

		# Look for all text files and assign new ledger instance as
		# the previous ledger file number + 1. 
		# Eg: If myledger2.txt exists, then create myledger3.txt
		# When used again.
		# If first time being used, just start off with myledger1.txt
		existing_ledgers = []
		for ledger in glob.glob("*.txt"):
			existing_ledgers.append(ledger)

		if existing_ledgers:
			last_ledger = int(re.findall(r'\d+', existing_ledgers[-1])[0])
			self._name = "myledger{}.txt".format(last_ledger+1)
		else:
			self._name = "myledger1.txt"

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

"""
Improvements:
1. Add delete entry option
2. User is able to display what ledger they want
3. Different table formats
"""