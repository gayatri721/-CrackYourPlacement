def isPossible(a,b,n,k):

	# Sort the array a[]
	# in decreasing order.
	a.sort(reverse=True)

	# Sort the array b[]
	# in increasing order.
	b.sort()

	# Checking condition
	# on each index.
	for i in range(n):
		if (a[i] + b[i] < k):
			return False

	return True


# Driver code

a =list(map(int,input().split()))
b = list(map(int,input().split()))
k = int(input())
n =len(a)

if(isPossible(a, b, n, k)):
	print("Yes")
else:
	print("No")

