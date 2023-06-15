# Binary search is an algorithm finding a given position in a sorted array
# The algorithm processes comparing the value (X) needed to find and the middle value (M) in the array
# If X < M --> We need to find the first half of the array
# If X > M --> We need to find the later half of the array
def first_pos(array, n):
	left, right = 0, len(array) - 1
	res = 0
	while left <= right:
		middle = (left + right) // 2
		if n == array[middle]:
			res = middle
			right = middle - 1
		elif n < array[middle]:
			right = middle - 1
		elif n > array[middle]:
			left = middle + 1
	return res

def last_pos(array, n):
	left, right = 0, len(array) - 1
	res = 0
	while left <= right:
		middle = (left + right) // 2
		if n == array[middle]:
			res = middle
			left = middle + 1
		elif n < array[middle]:
			right = middle - 1
		elif n > array[middle]:
			left = middle + 1
	return res

if __name__ == '__main__':
	array = [1, 1, 2, 2, 2, 3, 4, 5, 5]
	n = int(input())
	array.sort()
	print(array)
	print(first_pos(array, n))
	print(last_pos(array, n))