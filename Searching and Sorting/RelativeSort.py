"""Given two arrays arr1 and arr2, the elements of arr2 are distinct,
and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering 
of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

 

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]"""


def relativeSortArray(A1, A2):
    freqMap = {}
    sortedArr = []

    # Step 1: Create a frequency map of the elements in A2
    # This freqMap could be used to store the frequency of each element in A1
    for i in A2:
        freqMap[i] = A1.count(i)
    print(freqMap)

    # Step 2: Adding the element to the sorted array as per the order in the array2
    # Second loop has the TC of O(A1.count(element of A2)), element will be added freqMap[i] times
    for i in A2:
        for j in range(freqMap[i]):
            sortedArr.append(i)
    print(sortedArr)

    # Step 3: Adding the elements that are not in the array2 to the sorted array
    # These elements should be in increasing order (as per the question)
    remainingeElements = [i for i in A1 if i not in sortedArr]
    remainingeElements.sort()
    sortedArr.extend(remainingeElements)
    return sortedArr


A1, A2 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]
print(relativeSortArray(A1, A2))
