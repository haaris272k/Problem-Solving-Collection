"""Given an array arr[] of N integers. The task is to sort the array arr[] according to the frequency of elements in decreasing order. 
Note: If the frequencies of the two elements are the same, 
then the smaller element should come first.

Examples:  

Input: arr[] = { 4, 4, 5, 6, 4, 2, 2, 8, 5 } 
Output: 4 4 4 2 2 5 5 6 8

Input: arr[] = { 9, 9, 5, 8, 5 } 
Output: 5 5 9 9 8 
  """


# arr = [4, 4, 5, 6, 4, 2, 2, 8, 5]
arr = [9, 9, 5, 8, 5]

FrequencyMap = {}
for i in arr:
    if i not in FrequencyMap:
        FrequencyMap[i] = 1
    else:
        FrequencyMap[i] += 1
print(FrequencyMap)
Array = list(FrequencyMap.items())

Sorting = sorted(Array, key=lambda x: (-x[1], x[0]))

FinalAns = []
for k, v in Sorting:
    for i in range(v):
        FinalAns.append(k)
print(FinalAns)
