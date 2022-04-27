"""Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.

 

Example 1:

Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2."""


def solution(arr):
    keyequalsvalue = []
    hashtable = {i: arr.count(i) for i in arr}
    for k, v in hashtable.items():
        if k == v:
            # storing all the lucky integers
            keyequalsvalue.append(k)
    # checking whether there is any lucky inteher or not
    if keyequalsvalue:
        # finding the max lucky integer from all the lucky integers
        return max(keyequalsvalue)
    return -1


arr = [1, 2, 2, 3, 3, 3]
print(solution(arr))
