"""
Given string str, transform it according to the following rules:
Delete all the vowels from the string.
Insert # in front of all the consonants.
Change the case of all the letters of the string. 

Input:
str = aBAcAba
Output: #b#C#B
Explanation: Vowels at position 0,2,4,6 are deleted.
'#' is added before consonants at position 1,3,5 
and their case is changed.
"""


def problem(Str):
    for i in Str:
        if (
            i == "a"
            or i == "e"
            or i == "i"
            or i == "o"
            or i == "u"
            or i == "A"
            or i == "E"
            or i == "I"
            or i == "O"
            or i == "U"
        ):
            Str = Str.replace(i, "")
    hashtrick = "#"
    for j in Str:
        hashtrick = hashtrick + j + "#"
    final_string = hashtrick[0:-1].swapcase()
    if len(final_string) == 0:
        return "Empty String"
    return final_string


Str = input("Enter the string: ")
print(problem(Str))
