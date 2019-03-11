#!/usr/bin/env python
# -*-coding:utf-8-*-
# author:Mark.Qin

# Fibonacci series: F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*)

def fibonacci_series(n):
	if n < 1:
		raise Exception("Parameter Error, n should lt 3")
	a, b = 0, 1
	while a < n:
		print(a, end=",")
		a,b = b, a+b
		return a


def for_else():
	for n in range(2, 10):
		for x in range(2, n):
			if n % x == 0:
				print(n, 'equals', x, '*', n // x)
				break
		else:
		# loop fell through without finding a factor
			print(n, 'is a prime number')


def make_incr(n):
	return lambda x: x+n


if __name__ == '__main__':
	f = make_incr(42)
	print(f(1))


