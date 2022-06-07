"""Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become ""."""


s = "a#c"
t = "b"

stack1 = []
stack2 = []

for i in range(len(s)):

    if s[i] == "#":
        # if the character is a backspace then pop the last element from the stack
        # i.e the element which was added last
        if stack1:
            stack1.pop()
    else:
        # else keep adding the character to the stack
        stack1.append(s[i])

for i in range(len(t)):

    if t[i] == "#":

        if stack2:
            stack2.pop()

    else:
        stack2.append(t[i])

print(stack1 == stack2)
