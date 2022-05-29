"""Given an array of names (consisting of lowercase characters) of candidates in an election.
A candidate name in array represents a vote casted to the candidate. Print the name of candidate that received Max votes.
If there is tie, print lexicographically smaller name.

Example 1:

Input:
n = 13
Votes[] = {john,johnny,jackie,johnny,john 
jackie,jamie,jamie,john,johnny,jamie,
johnny,john}
Output: john 4"""

from collections import Counter



def maximum_vote(array):
    finding_freq = Counter(array)
    maximum = max(finding_freq.values())
    sorting = sorted(finding_freq.items())
    for key, val in sorting:
        if val == maximum:
            return (key, val)


# array = ["andy", "blake", "clark", "blake", "blake"]
array = input().split()
print(maximum_vote(array))
