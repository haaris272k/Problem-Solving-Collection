"""You are given an integer array ranks and a character array suits. 
You have 5 cards where the ith card has a rank of ranks[i] and a suit of suits[i].

The following are the types of poker hands you can make from best to worst:

"Flush": Five cards of the same suit.
"Three of a Kind": Three cards of the same rank.
"Pair": Two cards of the same rank.
"High Card": Any single card.
Return a string representing the best type of poker hand you can make with the given cards.

Note that the return values are case-sensitive.

 

Example 1:

Input: ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"]
Output: "Flush"
Explanation: The hand with all the cards consists of 5 cards with the same suit, so we have a "Flush"."""

ranks = [10, 10, 2, 12, 9]
suits = ["a", "b", "c", "a", "d"]

ForFlush, ForThreeofAKind, ForPair = False, False, False


# For Flush
suit = suits[0]
if all(suit == suits[i] for i in range(len(suits))):
    ForFlush = True

# For Three of a Kind and Pair

NofKind = {}
for i in range(len(ranks)):
    if ranks[i] in NofKind:
        NofKind[ranks[i]] += 1
    else:
        NofKind[ranks[i]] = 1

for rank, rankcount in NofKind.items():
    if rankcount >= 3:
        ForThreeofAKind = True
        break
    elif rankcount == 2:
        ForPair = True
        break

if ForFlush == True:
    print("Flush")
elif ForThreeofAKind == True:
    print("Three of a Kind")
elif ForPair == True:
    print("Pair")
else:
    print("High Card")
