s = "loveleetcode"
c = "e"
s = "aaab"
c = "b"
idxlist = [i for i in range(len(s)) if s[i] == c]
# print(idxlist)

distance = []
for pos, char in enumerate(s):
    position = position
    temp = []
    for posi_c in idxlist:
        dist = abs(position - posi_c)
        # finding minimum distance of each char from the c
        temp.append(dist)
    distance.append(min(temp))
print(distance == [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0])
