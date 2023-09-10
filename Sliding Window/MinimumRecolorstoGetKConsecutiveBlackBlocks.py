"""You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B',
representing the color of the ith block. The characters 'W' and 'B' denote the colors white 
and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least
one occurrence of k consecutive black blocks.

 

Example 1:

Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW". 
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3."""


# blocks = "WBBWWBBWBW"
# k = 7
blocks = "WBWBBBW"
k = 2
n = len(blocks)
count_white_in_each_window = []
start, end = 0, 0
while end < len(blocks):
    if end - start + 1 == k:
        substr = blocks[start : end + 1]
        if len(set(substr)) == "B":
            count_white_in_each_window.append(0)
        else:
            count_white_in_each_window.append(substr.count("W"))
        start += 1
    end += 1
print(count_white_in_each_window)
print(min(count_white_in_each_window))
