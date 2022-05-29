"""Given a list of N words. 
Count the number of words that appear exactly twice in the list.

Example 1:

Input:
N = 3
list = {Geeks, For, Geeks}
Output: 1
Explanation: 'Geeks' is the only word that 
appears twice. 

"""


from collections import Counter

List = input().split()
em = []
freq = Counter(List)
for i, j in freq.items():
    if j == 2:
        em.append(i)
print(len(em))
