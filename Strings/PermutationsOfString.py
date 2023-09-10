# Find all permutations of a string
from itertools import permutations


s = "ABC"

ans = permutations(s)
lst=[]
for i in ans:
    
    lst.append("".join(i))
print(lst)
