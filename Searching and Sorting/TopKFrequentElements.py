nums = [1, 1, 1, 2, 2, 3]
k = 2
import heapq

CountMap = {}
final_ans = []

# making a count map
for i in nums:
    if i in CountMap:
        CountMap[i] += 1
    else:
        CountMap[i] = 1

# Sorting keys on the basis of increasing frequency
ans = sorted(CountMap.items(), key=lambda x: (-x[1], x[0]))

# getting top k elements by iterating through the list up to k
for i in range(k):
    final_ans.append(ans[i][0])
print(final_ans)

# Alternative solution using heapq
# Line 17 to 20 could be replaced with:
ans = heapq.nlargest(k, CountMap, key=CountMap.get)
print(ans)
