def insertionSort(A):
	for i in xrange(1, len(A)):
		shouldShift = False
		for j in xrange(0, i + 1):
			if A[i] < A[j]:
				shouldShift = True
				break

		tmp = A[i]

		for k in xrange(i, j, -1):
			A[k] = A[k - 1]

		A[j] = tmp

	return A
