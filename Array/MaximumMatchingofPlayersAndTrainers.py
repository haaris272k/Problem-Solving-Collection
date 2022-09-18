"""You are given a 0-indexed integer array players, where players[i] represents the ability of the ith player. You are also given a 0-indexed integer array trainers, where trainers[j] represents the training capacity of the jth trainer.

The ith player can match with the jth trainer if the player's ability is less than or equal to the trainer's training capacity. Additionally, the ith player can be matched with at most one trainer, and the jth trainer can be matched with at most one player.

Return the maximum number of matchings between players and trainers that satisfy these conditions.

 

Example 1:

Input: players = [4,7,9], trainers = [8,2,5,8]
Output: 2
Explanation:
One of the ways we can form two matchings is as follows:
- players[0] can be matched with trainers[0] since 4 <= 8.
- players[1] can be matched with trainers[3] since 7 <= 8.
It can be proven that 2 is the maximum number of matchings that can be formed."""


players = [4, 7, 9]  # ability of the ith player
trainers = [8, 2, 5, 8]  # capability of the ith trainer

players = [1, 1, 1]
trainers = [10]

players = [1, 10000]
trainers = [10000, 1]

# Brute force
# O(n^2)
cnt = 0
max_count = 0
for i in set(players):
    ele = i
    for j in trainers:
        if ele <= j:
            cnt += 1
            break
    max_count = max(max_count, cnt)
print(max_count)

# Optimized
players.sort()
trainers.sort()

p = len(players)
t = len(trainers)

pointer1 = 0  # pointer for players
pointer2 = 0  # pointer for trainers
match_count = 0

while pointer1 < p and pointer2 < t:
    if players[pointer1] <= trainers[pointer2]:
        match_count += 1
        pointer1 += 1  # if match is found then means increase both the pointers
        pointer2 += 1
    else:
        pointer2 += 1  # if match is not found then increase the pointer2 to compare for more elements
print(match_count)
