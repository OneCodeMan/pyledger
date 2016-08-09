import ledger as l
import sys
import time

print("Creating new ledger...")
time.sleep(2)

led = l.Ledger()
running = True

while running:
	print("(Enter 0 0 to quit)")
	item, price = input("Enter an item and price, separated by a space. (eg: item1 10):\n").split()

	if item == "0" and int(price) == 0:
		print("Bye")
		sys.exit()

	led.add(item, float(price))
	led.display_ledger()
