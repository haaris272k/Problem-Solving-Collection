"""Given a sentence text (A sentence is a string of space-separated words) in the following format:

First letter is in upper case.
Each word in text are separated by a single space.
Your task is to rearrange the words in text such that all words are rearranged in an increasing order of their lengths. If two words have the same length, arrange them in their original order.

Return the new text following the format shown above.

 

Example 1:

Input: text = "Leetcode is cool"
Output: "Is cool leetcode"
Explanation: There are 3 words, "Leetcode" of length 8, "is" of length 2 and "cool" of length 4.
Output is ordered by length and the new first word starts with capital letter."""

text = "Leetcode is cool"
to_list = text.split()

lst2 = []
for i in to_list:

    lst2.append([i, len(i)])

arrange = sorted(lst2, key=lambda x: x[1])

string = ""
for i in arrange:

    string += i[0] + " "

print(string.capitalize().rstrip())
