"""You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

 

Example 1:

Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th]."""


from collections import OrderedDict


score = [10, 3, 8, 9, 4]
sort = sorted(score, reverse=True)
ranking = []
rankMap = OrderedDict()
for i in range(len(sort)):
    if i == 0:
        ranking.append("Gold Medal")
        rankMap[sort[i]] = ranking[i]

    elif i == 1:
        ranking.append("Silver Medal")
        rankMap[sort[i]] = ranking[i]

    elif i == 2:
        ranking.append("Bronze Medal")
        rankMap[sort[i]] = ranking[i]

    else:
        ranking.append(str(i + 1))
        rankMap[sort[i]] = ranking[i]

answer = []
for i in range(len(score)):

    answer.append(rankMap[score[i]])

print(answer)
