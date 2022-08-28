"""You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
 

Example 1:

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe"."""


s = "leet**cod*e"
my_stack = []

for i in range(len(s)):
    if s[i] != "*":
        my_stack.append(s[i])
    else:
        my_stack.pop()

ans = "".join(my_stack)
print(ans)

# to_lst = list(s)
# for i in range(len(to_lst)):
#     popped_char = to_lst.pop(0)
#     print(popped_char)
#     if popped_char == "*":
#         my_stack.pop()
#     else:
#         my_stack.append(popped_char)
# print(my_stack)
# ans = "".join(my_stack)
# print(ans)
