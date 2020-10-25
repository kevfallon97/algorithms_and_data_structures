import collections

# SOLUTION 1
def finder_1(arr1, arr2):
	
	arr1.sort()
	arr2.sort()
	for num1, num2, in zip(arr1, arr2):
		if num1 != num2:
			return num1
	return -1

# SOLUTION 2
def finder_2(arr1, arr2):

	for num in arr1:
		if num not in arr2:
			return num
	return -1

# SOLUTION 3
def finder_3(arr1, arr2):
	count = 0
	for i in arr1:
		for j in arr2:
			if i != j:
				count += 1
		if count == len(arr2):
			return i
		else:
			count = 0
	return -1

# SOLUTION 4
def finder_4(arr1, arr2):
	d = collections.defaultdict(int)
	for num in arr2:
		d[num] += 1

	for num in arr1:
		if d[num] == 0:
			return num
		else:
			d[num] -= 1

missing_elem = finder_1([1,2,3,4,5,6,7], [3,7,2,1,4,6])
print(f"{missing_elem} is the missing number.")

missing_elem = finder_2([1,2,3,4,5,6,7], [3,7,2,1,4,6])
print(f"{missing_elem} is the missing number.")

missing_elem = finder_3([1,2,3,4,5,6,7], [3,7,2,1,4,6])
print(f"{missing_elem} is the missing number.")

missing_elem = finder_4([1,2,3,4,5,6,7], [3,7,2,1,4,6])
print(f"{missing_elem} is the missing number.")