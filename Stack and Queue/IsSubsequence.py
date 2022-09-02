"""Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true"""


s = "bc"
t = "aahbgdc"

compare = s
s = s[::-1]
popper_stack = list(s)
final_checker_string = ""

# ignore function
def ignore():
    pass


for char in range(len(t)):
    # if stack is empty, just ignore (dont perform any operation)
    if len(popper_stack) == 0:
        ignore()

    # pop the top element from the stack and check if,
    # it is equal to the current character in the string t or not
    # if it is equal, then append it to the final_checker_string else,
    # (if it is not equal) push the popped element back to the stack and continue next iteration
    else:
        popped = popper_stack.pop()
        if popped == t[char]:
            final_checker_string += popped
        else:
            popper_stack.append(popped)

# finally, check if the final_checker_string is equal to the (given subsequence) or not
print(final_checker_string == compare)
