
class Node:
		def __init__(self, val):
			self.val = val
			self.next_node = None

class SinglyLinkedList:
	def __init__(self):
		self.head_val = None
		

	# Insert new node at front of SLL
	def insert_front(self, val):
		new_node = Node(val)
		new_node.next_node = self.head_val
		self.head_val = new_node

	# Insert new node at end of SLL
	def insert_end(self, val):
		new_node = Node(val)						
		if self.head_val is None:
			self.head_val = new_node
			return
		last_node = self.head_val					
		while last_node.next_node is not None:
			last_node = last_node.next_node
		last_node.next_node = new_node

	# Insert new node inbetween two nodes (insert behind prev_node)
	def insert_between(self, val, prev_val):
		new_node = Node(val)
		if self.head_val is not None:
				current_node = self.head_val
				while current_node.next_node is not None and current_node.val != prev_val:
					prev_node = current_node
					current_node = current_node.next_node						
				new_node.next_node = current_node.next_node
				current_node.next_node = new_node
				return None
		else:
			return None		

	# Removing a node from the SLL
	def remove_node(self, remove_val):
		current_node = self.head_val
		# check SLL is not empty						
		if current_node is not None:
			if current_node.val == remove_val:
				self.head = current_node.next
				return
			# find node to be removed			
			while current_node.next_node is not None and current_node.val != remove_val:
				prev_node = current_node
				current_node = current_node.next_node
			if current_node.val == remove_val:
				prev_node.next_node = current_node.next_node
			else:
				print("Removal key not found")
				return None
		else:
			print("Empty SLL")
			return None

	# Print the linked list
	def print_list(self):
		printval = self.head_val
		while printval is not None:
			print (printval.val)
			printval = printval.next_node


sll = SinglyLinkedList()
sll.insert_front("Tue")
sll.insert_front("Mon")
sll.insert_end("Thu")
sll.insert_between("Wed", "Tue")
sll.insert_end("Fri")
sll.print_list()

sll.remove_node("Tue")
sll.print_list()


# class Node(self):

# 	def __init__(self, value):
# 		self.value = value
# 		self.nextNode = None

# a = Node(1)
# b = Node(2)
# c = Node(3)

# a.nextNode = b
# b.nextNode = c