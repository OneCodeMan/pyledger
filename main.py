import ledger as l
import os

if os.path.exists("myledger.txt"):
	print("Let's get going")
	# Prompt for add
	# Every time they add, display
else:
	led = l.Ledger()
	led.display_ledger()
	led.add("item1", 200)
	led.display_ledger()