"""Given a string S. For each index i(1<=i<=N-1), erase it if s[i] is equal to s[i-1] 
in the string.

Example 1:

Input:
S = aabb
Output:  ab 
Explanation: 'a' at 2nd position is
appearing 2nd time consecutively.
Similiar explanation for b at
4th position."""

S = "aabbba"
S = list(S)  # convert string to list to make use of propery of stack
string = ""  # string to which non adjacent characters will be added
for i in range(len(S)):

    # pop the last element from the stack
    ele = S.pop()

    # if the last element in the string is the same as the current element in the stack
    # Do nothing
    if string and string[-1] == ele:
        pass

    else:
        # if the last element in the string is not the same as the current
        # element in the string then add the current element to the string
        string += ele

print(string)
