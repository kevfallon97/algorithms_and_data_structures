import anagram_check
import unittest

class TestAnagram(unittest.TestCase):

	# TEST CASES TAKEN FROM QUESTION
	# TEST FIRST SOLUTION
	def test_01(self):
		s1 = "public relations"
		s2 = "crap built on lies"
		self.assertTrue(anagram_check.anagram_1(s1,s2))

	def test_02(self):
		s1 = "clint eastwood"
		s2 = "old west action"
		self.assertTrue(anagram_check.anagram_1(s1,s2))

	def test_03(self):
		self.assertTrue(anagram_check.anagram_1('go go go','gggooo'))
		self.assertTrue(anagram_check.anagram_1('abc','cba'))
		self.assertTrue(anagram_check.anagram_1('hi man','hi     man'))
		self.assertFalse(anagram_check.anagram_1('aabbcc','aabbc'))
		self.assertFalse(anagram_check.anagram_1('123','1 2'))

	# TEST SECOND SOLUTION
	def test_04(self):
		s1 = "public relations"
		s2 = "crap built on lies"
		self.assertTrue(anagram_check.anagram_2(s1,s2))

	def test_05(self):
		s1 = "clint eastwood"
		s2 = "old west action"
		self.assertTrue(anagram_check.anagram_2(s1,s2))

	def test_06(self):
		self.assertTrue(anagram_check.anagram_2('go go go','gggooo'))
		self.assertTrue(anagram_check.anagram_2('abc','cba'))
		self.assertTrue(anagram_check.anagram_2('hi man','hi     man'))
		self.assertFalse(anagram_check.anagram_2('aabbcc','aabbc'))
		self.assertFalse(anagram_check.anagram_2('123','1 2'))


if __name__ == '__main__':
	unittest.main()