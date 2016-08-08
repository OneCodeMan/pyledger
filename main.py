import ledger as l
import os
import sys

if os.path.exists("myledger.txt"):
	print("Ledger already exists!")
	#Extract csv contents of already existing file
else:
	print("Creating new ledger")
	led = l.Ledger()
	running = True

	while running:
		print("(Enter 0 0 to quit)")
		item, price = input("Enter an item and price, separated by a space. (eg: item1, 10):\n").split()

		if item == "0" and int(price) == 0:
			sys.exit()

		led.add(item, price)
		led.display_ledger()
