
def find_max_min(list1):
	min_max = []

	if min(list1) == max(list1):
		return [len(list1)]

	min_max.append (min(list1))

	min_max.append (max(list1))
	return min_max

# print (min_max([4,4,4,4,4]))
