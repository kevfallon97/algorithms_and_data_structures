'''
Given a string of opening and closing parentheses, check whether it’s balanced. 
We have 3 types of parentheses: round brackets: 
(), square brackets: [], and curly brackets: {}. 
Assume that the string doesn’t contain any other character than these, 
no spaces words or numbers. 
As a reminder, balanced parentheses require every opening parenthesis 
to be closed in the reverse order opened. 
For example ‘([])’ is balanced but ‘([)]’ is not.

You can assume the input string has no spaces.
'''
# SOLUTION

from implementations.stack import Stack

def balance_check(s):

	# return false if length of s is odd
	if len(s) % 2 != 0:
		return False

	open_brackets = ['(','[','{']
	closing_brackets = [')',']','}']

	stack = Stack()

	
	# traverse through the string, push opening brackets to stack	
	for bracket in s:
		# if bracket is an open bracket, push to stack
		if bracket in open_brackets:
			stack.push(bracket)
		# if bracket is a closing bracket, pop the top of the stack and compare brackets
		else:
			# if stack is empty, there is a closing bracket with no opening bracket, return false
			if stack.isEmpty():
				return False
			# pop top element
			popped = stack.pop()
			# if the current bracket and the popped bracket are not matching pairs, return false
			if closing_brackets.index(bracket) != open_brackets.index(popped):
				return False
	return True




