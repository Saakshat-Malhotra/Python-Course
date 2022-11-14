import unittest
import script

class TestMain(unittest.TestCase):
	def test_do_stuff(self):
		test_param = 5
		result = script.do_stuff(test_param)
		self.assertEqual(result, 10)

	def test_do_stuff2(self):
		test_param = 'shfkjsd'
		result = script.do_stuff(test_param)
		self.assertIsInstance(result, ValueError)

	def test_do_stuff3(self):
		test_param = None
		result = script.do_stuff(test_param)
		self.assertEqual(result, 'please enter a number')

	def test_do_stuff4(self):
		test_param = ''
		result = script.do_stuff(test_param)
		self.assertEqual(result, 'please enter a number')


if __name__ == '__main__':
	unittest.main()