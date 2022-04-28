"""You have been given two arrays/list ‘ARR1’ and ‘ARR2’ consisting of ‘N’ and ‘M’ integers respectively. Your task is to return the number of elements common to ‘ARR1’ and ‘ARR2’ and the number of elements in the union of ‘ARR1’ and ‘ARR2’.
Example:
Let’s assume ‘ARR1’ is [1,2,3,4,5] and ‘ARR2’ is [2,4,6,8]. Elements common to ‘ARR1’ and ‘ARR2’ are [2,4] as they occur in both ‘ARR1’ and ‘ARR2’. Therefore the number of elements common to ‘ARR1’ and ‘ARR2’ is 2. Union of ‘ARR1’ and ‘ARR2’ is [1,2,3,4,5,6,8]. Therefore the number of distinct elements in the union of ‘ARR1’ and ‘ARR2’ is 7. So, the answer will be 2 7."""

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8]

# Brute force approach TC O(n^2)
# rtime 1232ms
c = 0
for i in arr1:
    if i in arr2:
        c += 1
my_set = set(arr1 + arr2)  # most optimal way of getting array of distinct elements
print([c, len(my_set)])


# Better approach using hashmap TC O(n^2)
# rtime 800ms
from collections import Counter

c = 0
htable = Counter(arr1)
for k, v in htable.items():
    if k in arr2:
        c += 1
my_set = set(arr1 + arr2)  # most optimal way of getting array of distinct elements
print([c, len(my_set)])
