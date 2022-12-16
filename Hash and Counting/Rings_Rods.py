# rings = "B0B6G0R6R0R6G9"
# rings = "B0R0G0R9R0B0G0"
rings = "G4"

color = [i for i in rings if i == "R" or i == "G" or i == "B"]
rodnumber = [
    i
    for i in rings
    if i == "0"
    or i == "1"
    or i == "2"
    or i == "3"
    or i == "4"
    or i == "5"
    or i == "6"
    or i == "7"
    or i == "8"
    or i == "9"
]

color_rod_map = {}
for i in range(len(color)):

    # if rod is not in the map
    # create a new list and append color to that rod number(which is a key)
    if rodnumber[i] not in color_rod_map:
        color_rod_map[rodnumber[i]] = [color[i]]
    # if rod is already in the map, add the color to the existing list
    else:
        color_rod_map[rodnumber[i]].append(color[i])


count_of_rods_with_3_colors = 0
for rodNumber, ringColor in color_rod_map.items():
    if len(set(ringColor)) == 3:
        count_of_rods_with_3_colors += 1
print(count_of_rods_with_3_colors)
