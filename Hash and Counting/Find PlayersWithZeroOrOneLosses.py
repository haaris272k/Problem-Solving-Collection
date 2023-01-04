'''You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.'''


matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
# matches = [[2,3],[1,3],[5,4],[6,4]]
from collections import Counter

# n=len(matches)
# winners=set()
# all_losers=[]
final_losers=[]

# # finding all losers
# for i in range(n):
#     all_losers.append(matches[i][1])

# # finding winners who won all the matches
# for i in range(n):
#     if matches[i][0] not in all_losers:
#         winners.add(matches[i][0]) 

# # finding losers who lost exactly one match
# freq=Counter(all_losers)
# for k,v in freq.items():
#     if v==1:
#         final_losers.append(k)

# # sorting the answer
# winners=sorted(list(winners))
# final_losers=sorted(list(final_losers))

# # final answer
# print([winners,final_losers])

win, lose = zip(*matches)
print(win)
print(lose)
winners=set(win)-set(lose)
lostonce=Counter(lose)
for k,v in lostonce.items():
    if v==1:
        final_losers.append(k)

print([sorted(winners),sorted(final_losers)])