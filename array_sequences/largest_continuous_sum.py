'''
PROBLEM 

Given an array of integers (positive and negative) find the largest continuous sum.
'''

# SOLUTION

def large_cont_sum(arr):
	# check if array is length 0
	if len(arr) == 0:
		return 0

	# start the max and current sum at the first element
	max_sum = arr[0]
	current_sum = arr[0]

	# for every element in array
	for num in arr[1:]:

		# set current sum as the higher of the two
		current_sum = max(current_sum+num, num)

		# set max as the higher between the current_sum and the current_max
		max_sum = max(current_sum, max_sum)
	return max_sum

print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))


