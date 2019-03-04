#!/usr/bin/env python
# -*-coding:utf-8-*-
# author:Mark.Qin

import unittest
from Number.number import Number

class TestNumber(unittest.TestCase):


	def test_init(self):
		n = Number(3, 2)
		self.assertEqual(n.a, 3)
		self.assertEqual(n.b, 2)
		self.assertTrue(isinstance(n,Number))

	def test_add(self):
		n = Number(3, 2)
		self.assertEqual(n.add(), 5)

	def test_minus(self):
		n = Number(3, 2)
		self.assertEqual(n.minus(), 1)

	def test_multiply(self):
		n = Number(3, 2)
		self.assertEqual(n.multiply(), 6)

	def test_division(self):
		n = Number(3, 2)
		self.assertEqual(n.division(), 1.5)

	def test_exact_division(self):
		n = Number(3, 2)
		self.assertEqual(n.exact_division(), 1)

	def test_mod(self):
		n = Number(5, 2)
		self.assertEqual(n.mod(), 1)

	def test_power(self):
		n = Number(3, 2)
		self.assertEqual(n.power(), 9)



if __name__ == '__main__':
	unittest.main()