"""Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers."""


arr = [1, 3, 5, 7, 9]
all_sums = []
# finding sum of numbers except one element
for i in range(len(arr)):
    # print(arr[:i] + arr[i + 1 :])
    all_sums.append(sum(arr[:i] + arr[i + 1 :]))
print(all_sums)
print(min(all_sums), max(all_sums))
