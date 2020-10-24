
class Stack:

	def __init__(self):
		self.items = []

	# returns True is stack is empty
	def isEmpty(self):
		return self.items == []

	# push item onto stack
	def push(self, item):
		self.items.append(item)

	# pop item from top of stack
	def pop(self):
		return self.items.pop()

	# view the top item
	def peek(self):
		return self.items[-1]

	# returns the length of the stack
	def size(self):
		return len(self.items)

