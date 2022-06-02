'''Given a string s, reverse the order of characters in each word within a sentence while 
still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"'''


s = "God Ding"
to_lst = s.split(" ")
new_string = ""

for i in range(len(to_lst)):

    new_string += to_lst[i][::-1] + " "

print(
    new_string[0:-1]
)  # printing without last space as it is not required as per the question
