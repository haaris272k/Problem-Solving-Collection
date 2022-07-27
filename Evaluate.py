# priorities = [1, 4, 8, 4]
priorities = [1, 3, 7, 3]
map = {}
for a, b in enumerate(priorities):
    if b not in map:
        map[b] = a + 1
    else:
        pass
print(map)

lst = []
for i in priorities:
    lst.append(map[i])
print(lst)
