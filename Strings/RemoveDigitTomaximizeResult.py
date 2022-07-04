"""You are given a string number representing a positive integer and a character digit.

Return the resulting string after removing exactly one occurrence of digit from number such that the value of the resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least once in number.

 

Example 1:

Input: number = "123", digit = "3"
Output: "12"
Explanation: There is only one '3' in "123". After removing '3', the result is "12"."""


number = "3123"
digit = "3"

toList = list(number)
numlist = []
for i in range(len(toList)):

    if toList[i] == digit:
        # adding elements except the digit for occurence one
        num = toList[:i] + toList[i + 1 :]
        # converting the list to string and then to int and appending to the list
        numlist.append(int("".join(num)))

print(str(max(numlist)))
