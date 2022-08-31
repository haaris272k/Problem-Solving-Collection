"""You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.

At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:

An integer x - Record a new score of x.
"+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
"D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
"C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.
Return the sum of all the scores on the record. The test cases are generated so that the answer fits in a 32-bit integer."""
ops = ["1", "C"]

# //reverse the array ops to strictly follow LIFO order for stack// #
ops = ops[::-1]
n = len(ops)
operated_list = []

# popping element from our stack and checking for the given conditions
for i in range(n):
    popped = ops.pop()
    if popped.isdigit() or popped.lstrip("-").isdigit():
        operated_list.append(int(popped))
    if popped == "C":
        operated_list.pop()
    if popped == "D":
        operated_list.append(2 * operated_list[-1])
    if popped == "+":
        summ_of_last_two = operated_list[-1] + operated_list[-2]
        operated_list.append(summ_of_last_two)
    print(operated_list)
print(sum(operated_list))
