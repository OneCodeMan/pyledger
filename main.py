import ledger as l
import os

if os.path.exists("myledger.txt"):
	print("Ledger already exists!")
	#display_ledger()
else:
	print("Creating new ledger")
	led = l.Ledger()
	#display_ledger()