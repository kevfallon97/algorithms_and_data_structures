'''
PROBLEM 2

Given an integer, create a function which returns the sum of all the
individual digits in that integer.
For example: if n = 4321, return 4+3+2+1
'''

def sum_func(n):
	
	# BASE CASE
	if n < 10:
		return n

	# RECURSIVE CALL
	return n%10 + sum_func(int(n/10)) 

print(sum_func(4321))