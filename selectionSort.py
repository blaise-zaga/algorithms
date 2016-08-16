def selectionSort(A):
	for i in xrange(0, len(A)):
		print A

		indexOfMinInUnsortedArray = i

		for j in xrange(i, len(A)):
			if A[j] < A[indexOfMinInUnsortedArray]:
				indexOfMinInUnsortedArray = j

		tmp = A[i]
		A[i] = A[indexOfMinInUnsortedArray]
		A[indexOfMinInUnsortedArray] = tmp
	return A
