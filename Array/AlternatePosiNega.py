# arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
arr = [3, 1, -2, -5, 2, -4]


# Approach 1:-------------------------

posi = [arr[i] for i in range(len(arr)) if arr[i] >= 0]
nega = [arr[i] for i in range(len(arr)) if arr[i] < 0]


finallist = [None] * len(arr)

for i in range(len(arr)):
    if i % 2 == 0:
        if posi:
            finallist[i] = posi.pop(0)
    else:
        if nega:
            finallist[i] = nega.pop(0)

print(finallist)

# Approach 2:-------------------------
finallist = []
posi = []
nega = []
for i in range(len(arr)):
    if arr[i] >= 0:
        posi.append(arr[i])
    else:
        nega.append(arr[i])
for i in range(len(posi)):
    finallist.append(posi[i])
    finallist.append(nega[i])
print(finallist)
