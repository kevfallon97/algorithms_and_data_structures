import unittest
import balanced_parentheses

class TestBalanced(unittest.TestCase):

	def test_true(self):
		s1 = '[]'
		s2 = '[(){[]}]'
		s3 = '{{{{}}}}'
		self.assertTrue(balanced_parentheses.balance_check(s1))
		self.assertTrue(balanced_parentheses.balance_check(s2))
		self.assertTrue(balanced_parentheses.balance_check(s3))

	def test_false(self):
		s1 = '['
		s2 = '[}'
		s3 = '{[}'
		self.assertFalse(balanced_parentheses.balance_check(s1))
		self.assertFalse(balanced_parentheses.balance_check(s2))
		self.assertFalse(balanced_parentheses.balance_check(s3))

if __name__ == '__main__':
	unittest.main()
