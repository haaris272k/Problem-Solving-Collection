import collections


nums = [0, 1, 2, 2, 4, 4, 1]
# nums = [29, 47, 21, 41, 13, 37, 25, 7]


freqmap = {}
resultList = []
res = -1
for i in nums:
    if i % 2 == 0:
        if i in freqmap:
            freqmap[i] += 1
        else:
            freqmap[i] = 1


try:
    maxed = max(freqmap.values())
except:
    res = res

for k, v in freqmap.items():
    if v == maxed:
        resultList.append(k)


if resultList:
    resultList.sort()
    res = resultList[0]
else:
    res = res

print(res)
