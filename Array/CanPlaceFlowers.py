# flowerbed = [1, 0, 0, 0, 1]
# n = 2
# flowerbed = [0, 0, 1, 0, 1]
# n = 1
flowerbed = [1, 0, 0, 0, 1, 0, 0]
n = 2
couldbeplanted = 0
last = len(flowerbed) - 1
for i in range(len(flowerbed)):
    if flowerbed[i] == 0:
        if ((i == 0) or (flowerbed[i - 1] == 0)) and (
            (i == last) or flowerbed[i + 1] == 0
        ):
            flowerbed[i] = 1
            couldbeplanted += 1


print(flowerbed)
if couldbeplanted >= n:
    print(True)
else:
    print(False)
