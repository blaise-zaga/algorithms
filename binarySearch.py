# array A contains a sorted list of items
# x is the value that is being searched for
# returns the index at which the element being searched for is seen
# or -1 if the element is not found
def binarySearch(A, x):
	lowerBound = 0
	upperBound = len(A)
	while True:
		midpoint = (upperBound + lowerBound) / 2

		if A[midpoint] == x:
			return midpoint
		elif upperBound < lowerBound:
			return -1
		elif A[midpoint] < x:
			lowerBound = midpoint + 1
		elif A[midpoint] > x:
			upperBound = midpoint - 1
