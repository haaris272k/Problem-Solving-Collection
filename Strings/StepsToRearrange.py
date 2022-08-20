"""You are given a binary string s. In one second, all occurrences of "01"
are simultaneously replaced with "10". This process repeats until no occurrences 
of "01" exist.

Return the number of seconds needed to complete this process."""

# steps to remove all "01" and replace with "10"
# 1. find all "01"
# 2. replace all "01" with "10"
# 3. repeat until no "01"
# 4. return number of steps


def steps(s):
    steps = 0
    while "01" in s:
        s = s.replace("01", "10")
        steps += 1
    return steps


s = "11100"

print(steps(s))
