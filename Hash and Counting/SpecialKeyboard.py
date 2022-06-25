"""Imagine you have a special keyboard with all keys in a single row. The layout of characters on a keyboard is denoted by a string S1 of length 26. S1 is indexed from 0 to 25. Initially, your finger is at index 0.
To type a character, you have to move your finger to the index of the desired character. The time taken to move your finger from index i to index j is |j-i|, where || denotes absolute value.Find the time taken to type the string S2 with the given keyboard layout.


Example 1:

Input: 
S1 = "abcdefghijklmnopqrstuvwxyz"
S2 = "cba"
Output: 
4
Explanation:
Initially we are at index 0. To type 'c',
it will take a time of abs(0-2) = 2. To, type
'b' next, it will take abs(2-1) = 1. And, for
'a', it will take abs(1-0) = 1 unit time.
So, total time = 2+1+1 = 4."""


S1 = "abcdefghijklmnopqrstuvwxyz"
S2 = "cba"
map = {}
initial = 0
distance = []
for i in range(26):
    map[S1[i]] = i
print(map)
for i in S2:
    print(i)
    distance.append(abs(map[i] - initial))
    initial = map[i]
print(distance)
