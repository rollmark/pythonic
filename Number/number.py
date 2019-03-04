#!/usr/bin/env python
# -*-coding:utf-8-*-
# author:Mark.Qin


class Number:

	# Python Number
		# immutable
		# int
		# float
		# complex



	def __init__(self, a, b):
		self.a = a
		self.b = b

	def add(self):
		return self.a + self.b

	def minus(self):
		return self.a - self.b

	def multiply(self):
		return self.a * self.b

	def division(self):
		if self.b == 0:
			raise ZeroDivisionError
		return self.a / self.b

	def floor_division(self):
		if self.b == 0:
			raise ZeroDivisionError
		return self.a // self.b

	def mod(self):
		if self.b == 0:
			raise ZeroDivisionError
		return self.a % self.b

	def power(self):
		return self.a ** self.b


