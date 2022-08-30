"""A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.

 

Example 1:

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode"."""

s = "leeetcode"

if len(s) == 1 or len(s) == 2:
    print(s)
else:
    # putting characters of string to a stack
    popper_stack = list(s[::-1])

    # taking a list to store the characters
    string_list = [0] * len(popper_stack)

    # to ignore zeroes in the list
    ignore_zero = len(popper_stack)

    for i in range(len(s)):
        # popping the last character of the stack
        popped = popper_stack.pop()
        # checking if the last two characters and the popped character are same or not
        # if same then we will not add the popped character to the list
        # if not same then we will add the popped character to the list
        if string_list[-1] == string_list[-2] == popped:
            continue
        else:
            string_list.append(popped)

    print("".join(string_list[ignore_zero:]))
