"""
Linear Search Algorithm
TC: O(n)

"""

a = [1, 2, 3, 4, 5]
k = 2
n = len(a)

# General method
for i in range(n):

    if a[i] == k:

        print(i)

        break

# Pythonic method using index function
if k in a:

    print(a.index(k))

else:

    print("Not found")
