"""You have a chat log of n messages. You are given two string arrays messages and senders where messages[i] is a message sent by senders[i].

A message is list of words that are separated by a single space with no leading or trailing spaces. The word count of a sender is the total number of words sent by the sender. Note that a sender may send more than one message.

Return the sender with the largest word count. If there is more than one sender with the largest word count, return the one with the lexicographically largest name.

Note:

Uppercase letters come before lowercase letters in lexicographical order.
"Alice" and "alice" are distinct.
 

Example 1:

Input: messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"], senders = ["Alice","userTwo","userThree","Alice"]
Output: "Alice"
Explanation: Alice sends a total of 2 + 3 = 5 words.
userTwo sends a total of 2 words.
userThree sends a total of 3 words.
Since Alice has the largest word count, we return "Alice"."""


messages = ["How is leetcode for everyone", "Leetcode is useful for practice"]
senders = ["Bob", "Charlie"]

WordcountMap = {}
for i in range(len(senders)):
    # WordcountMap.update({senders[i]: messages[i]})
    if senders[i] in WordcountMap:
        WordcountMap[senders[i]] += " " + messages[i]
    else:
        WordcountMap[senders[i]] = messages[i]
print(WordcountMap)

# sender with the largest word count
# appending senders name lexiographically in the list
res = []
for key, value in WordcountMap.items():
    res.append((key, value.count(" ") + 1))
res = sorted(res, key=lambda item: (item[1], item[0]), reverse=True)
print(res[0][0])
