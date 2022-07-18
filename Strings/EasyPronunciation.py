"""Words that contain many consecutive consonants, like "schtschurowskia", are generally considered somewhat hard to pronounce.

We say that a word is hard to pronounce if it contains 4 or more consonants in a row; otherwise it is easy to pronounce. For example, "apple" and "polish" are easy to pronounce, but "schtschurowskia" is hard to pronounce.

You are given a string S consisting of N lowercase Latin characters. Determine whether it is easy to pronounce or not based on the rule above — print YES if it is easy to pronounce and NO otherwise.

For the purposes of this problem, the vowels are the characters {a,e,i,o,u} and the consonants are the other 21 characters."""


s = "schtschurowskia"

consecutive_consonants = 0
consecutive_consonants_list = []

ans = True

for i in range(len(s)):
    if s[i] in "bcdfghjklmnpqrstvwxyz":
        consecutive_consonants += 1
    else:
        consecutive_consonants_list.append(consecutive_consonants)
        consecutive_consonants = 0
consecutive_consonants_list.append(consecutive_consonants)
for i in consecutive_consonants_list:
    if i >= 4:
        ans = False
        break
if ans == True:
    print("YES")
else:
    print("NO")
