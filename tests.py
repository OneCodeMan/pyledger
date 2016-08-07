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



if __name__ == '__main__':
	unittest.main()