"""Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]"""


# arr = [1, 2, 3, 4, 5]
# k = 4
# x = 3
arr = [1, 1, 1, 10, 10, 10]
k = 1
x = 9
diff_list = []
for i in arr:
    diff_list.append([i, abs(i - x)])

custom_sort = sorted(diff_list, key=lambda x: x[1])
print(custom_sort)

ans = []
for i in range(k):
    ans.append(custom_sort[i][0])
ans.sort()
print(ans)
