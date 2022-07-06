"""Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

 

Example 1:

Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode"."""
s = "abBAcC"

stack = [None] * len(s)  # mandatory to initialize the stack with length of s

for i in range(len(s)):
    if stack[-1] == s[i].swapcase():

        # if the last element in the stack is the same as the
        # current element in the string but in opposite case,
        # then pop the last element from the stack
        stack.pop()

    else:
        # if the last element in the stack is not the same as the
        # current element in the string, then push the current element
        # to the stack
        stack.append(s[i])
        print(stack)

print(stack)
str = ""
for i in stack:
    if i is not None:
        str += i
print(str)
