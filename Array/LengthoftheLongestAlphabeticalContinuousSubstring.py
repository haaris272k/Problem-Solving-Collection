"""An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".

For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.
Given a string s consisting of lowercase letters only, return the length of the longest alphabetical continuous substring.

 

Example 1:

Input: s = "abacaba"
Output: 2
Explanation: There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
"ab" is the longest continuous substring."""


s = "orcvscn"
string_list = list(s)
for i in range(len(string_list)):
    string_list[i] = ord(string_list[i])
print(string_list)


# Logic of longest consecutive subsequence

curr_seq, max_seq = 1, 1
for i in range(1, len(string_list)):
    if string_list[i] == string_list[i - 1] + 1:
        curr_seq += 1

        max_seq = max(max_seq, curr_seq)
    else:
        curr_seq = 1

print(max(curr_seq, max_seq))
