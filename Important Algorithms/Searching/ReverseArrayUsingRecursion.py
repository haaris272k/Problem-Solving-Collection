"""Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory."""


"""
Key points :No extra memory is allowed.
            No inbuilt functions are allowed.
            Follow the algorithm which is the common approach to solve array reversal problem.
            Recursion, Two Pointers, Constant Space.
            TC : O(n)
            SC : O(1)
"""


def reverseArray(s, start, end):
    if start >= end:
        return

    s[start], s[end] = s[end], s[start]
    reverseArray(s, start + 1, end - 1)
    return s


s = ["h", "e", "l", "l", "o"]
start = 0
end = len(s) - 1
print(reverseArray(s, start, end))
