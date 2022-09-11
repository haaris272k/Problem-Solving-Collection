"""Given a string s, partition the string into one or more substrings
such that the characters in each substring are unique.
That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition."""

# s = "abacaba"
s = "hdklqkcssgxlvehva"
# making stack of string
stringStack = list(s)[::-1]
partition_list = []
temp = ""

for i in range(len(s)):
    # popping the last element of stack and adding it to temp if it is not in temp
    popped = stringStack.pop()
    if popped not in temp:
        temp += popped
    # as soon as we get a duplicate, we add the temp to partition_list and reset temp
    else:
        partition_list.append(temp)
        temp = popped

# adding the last temp to partition_list
partition_list.append(temp)
print(len(partition_list))
