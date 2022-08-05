from collections import defaultdict

sick = defaultdict(int)
for _ in range(int(input())):
    sick[input()] += 1
print(len(sick))
