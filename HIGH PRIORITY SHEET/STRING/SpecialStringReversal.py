"""Given a string S, containing special characters and all the alphabets, reverse the string without
affecting the positions of the special characters."""

s = "A&x#"

string_array = list(s)
alphabets_only = []

# Reversing snippet
for i in s:
    if i >= "a" and i <= "z" or i >= "A" and i <= "Z":
        alphabets_only.append(i)
rev = alphabets_only[::-1]
print(rev)

# putting alphabets back in original string (string_array)
ptr = 0
for i in range(len(s)):
    if string_array[i].isalpha():
        string_array[i] = rev[ptr]
        ptr += 1

print("".join(string_array))
