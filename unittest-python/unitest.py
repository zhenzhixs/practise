# -*- coding: utf-8 -*-
# Unittest 1.0 
# Author: Hai Feng

import sys
import unittest

class AddTest(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	def test_add(self):
		self.a = sum
		self.assertEqual(self.a(1,2),3)
		# print sum(1,2)

	# def test_sub(self):
		# self.assertEqual(1,2)
		# pass

def sum(x,y):
	return x+y

def sub(x,y):
	return x-y

# if __name__ == '__main__':
# 	unittest.main()
	# unittest.TestProgram()
	# help(getattr(unittest,"TestCase"))
	# help(unittest.TestCase)
	# print unittest.TestCase.__doc__
	# print dir(unittest)


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(AddTest)
	unittest.TextTestRunner(verbosity=2).run(suite)