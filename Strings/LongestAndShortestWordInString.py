"""Find longest and shortest word in a string"""
"""Input : "This is a test string"
Output : Minimum length word: a
         Maximum length word: string"""


s = "This is a test string"
toList = s.split()
print(toList)
countmap = {}
for i in toList:
    countmap[i] = len(i)

maxed = max(list(countmap.values()))
mini = min(list(countmap.values()))

for word, length in countmap.items():
    if length == maxed:
        print(f"Maxed Word is of length {maxed} and is :", word)
    if length == mini:
        print(f"Mini word is of length {mini} and is :", word)
