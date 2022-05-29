a = {89, 24, 75, 11, 23}
b = {89, 2, 4}
from collections import Counter

new = []
freq1 = Counter(a)
for k, v in freq1.items():
    if k in b:
        new.append(k)
print(new)