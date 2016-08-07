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
//      Code Buddha blesses this code to be bug free.
//
"""
LINES = "-" * 50

class Ledger:

	def __init__(self):

		self.total = 0
		self.head = "ITEM \t\t\t| PRICE\n{}".format(LINES)
		self.body = ""
		self.legs = "{}\nTOTAL: \t\t\t| {}\n".format(LINES, self.total)

		# For CSV
		self.entries = []

	def add(self, item, price):
		self.entries.append([item, price])
		self.body += "{} \t\t\t| {}\n".format(item, price)
		self.total += price
		self.legs = "{}\nTOTAL: \t\t\t| {}\n".format(LINES, self.total)

	def display_ledger(self):
		print("{} \n {} \n{}".format(self.head, self.body, self.legs))

	def get_entries(self):
		print("Entries: {}".format(self.entries))

	def get_total(self):
		print("Total: {}".format(self.total))

led = Ledger()
led.add("item1", 200)
led.add("item2", 500)
led.add("item2", 500)
led.add("item2", 500)
led.add("item2", 500)
led.add("item2", 500)
led.add("item2", 500)
led.get_entries()
led.display_ledger()
led.get_total()