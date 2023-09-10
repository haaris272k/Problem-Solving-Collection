"""A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".
Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc"."""

# s = "xyzzaz"
s = "aababcabc"
c, i, j = 0, 0, 0
window = 3

# In case of sliding window its mandatory to specify that till where
# the window should be considered
# It squite obvious that the size of the end of the window should be less than
# the size of the array/string
while j < len(s):
    # check if the window is of size to our desired window size
    if (j - i + 1) == window:
        # finding substring in window size (i and j will be the valid index for the window size)
        substr = s[i : j + 1]
        # condition check
        if len(set(substr)) == window:
            c += 1
        # after the condition check, increment the window size by 1
        # for both i and j (start and end)
        i += 1
        j += 1
    else:
        # if the window is not of size to our desired window size,
        # increment the end of the window by 1
        j += 1
print(c)
