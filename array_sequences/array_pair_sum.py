'''
ARRAY PAIR SUM

PROBLEM STATEMENT
Given an integer array, output all the unique pairs that sum to a specific value k.

So the input:
pair_sum([1,3,2,2], 4)

would return 2 pairs:
(1,3)
(2,2)

Note: For testing purposes, return the number of pairs identified
'''

# SOLUTION
def pair_sum(nums, k):

	pairs = set()								# hold unique pairs in set
	for i, numA in enumerate(nums[:-1]):		# for every elem in list, check for pair with remaining elements
		for numB in nums[i+1:]:					
			if numA + numB == k:				# check if pair sum to k
				pairs.add((numA, numB))			# add valid pair provided they are unique								
	return pairs								# return set of unique pairs


nums = [1,3,2,2,2]
pairs = pair_sum(nums, 4)
print(f"Number of pairs: {len(pairs)}")
print(f"Unique pairs: {pairs}")

