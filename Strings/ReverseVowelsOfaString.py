'''Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

 

Example 1:

Input: s = "hello"
Output: "holle"'''


s = "hello"


chrlst = []
idxlst = []
charidxlst = []
s = list(s)
vowel_set = set("aeiouAEIOU")

# finding vowels and their indices and storing them in a list
for idx, char in enumerate(s):
    if char in vowel_set:
        chrlst.append(char)
        idxlst.append(idx)

# append the vowels with the by reversing the indices list (idxlst)
idxlst = idxlst[::-1]
for i in range(len(idxlst)):
    charidxlst.append((chrlst[i], idxlst[i]))
print(charidxlst)
# finally, replace the vowels with the reversed vowels in the original stringlist
# and join them to form a string
for char, idx in charidxlst:
    s[idx] = char
print("".join(s))
