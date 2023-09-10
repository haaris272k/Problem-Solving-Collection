"""ou are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

 

Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone."""


import heapq

stones = [2, 7, 4, 1, 8, 1]
st = []

# create a max heap
for s in stones:
    heapq.heappush(st, -s)

# pop the two largest stones and smash them together
# if the result is not 0, push it back to the heap
# repeat until there is only one stone left
while len(st) > 1:
    # popp the two largest stones
    # and smash them together
    a = heapq.heappop(st)
    b = heapq.heappop(st)

    # if they are not equal, put the difference back
    difference = abs(a - b)
    if difference > 0:
        heapq.heappush(st, -difference)

# if there is only one stone left, return it
if st:
    print(-heapq.heappop(st))
else:
    print(0)