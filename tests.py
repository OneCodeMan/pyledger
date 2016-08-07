import unittest
import ledger as l

led = l.Ledger()
led2 = l.Ledger(200)

class TestLedgerClass(unittest.TestCase):

	def test_initial_total_zero(self):
		self.assertEqual(led.total, 0)

	def test_initial_total_not_zero(self):
		self.assertEqual(led2.total, 200)

	def test_head(self):
		self.assertEqual(led.head, "ITEM \t PRICE")

	def test_body_initial(self):
		self.assertEqual(led.body, "")

	def test_legs_initial(self):
		self.assertEqual(led.legs, "TOTAL: \t {}".format(led.total))

	#def test_prices_equal_total(self):


if __name__ == '__main__':
	unittest.main()