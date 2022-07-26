"""You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists
a direct path going from cityAi to cityBi.
Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore,
there will be exactly one destination city.

 

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is 
the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo"."""


# paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
# paths = [["B", "C"], ["D", "B"], ["C", "A"]]
paths = [["A", "Z"]]

cityMapping = {}
for path in paths:
    cityMapping[path[0]] = path[1]
print(cityMapping)

cityA = cityMapping.keys()
cityB = cityMapping.values()

print(cityA)
print(cityB)

# for i in cityB:
#     if i not in cityA:
#         print(i)

destCity = list(set(cityB) - set(cityA))[0]
print(destCity)
