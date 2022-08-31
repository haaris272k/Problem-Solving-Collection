"""The Leetcode file system keeps a log each time some user performs a change folder operation.

The operations are described below:

"../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
"./" : Remain in the same folder.
"x/" : Move to the child folder named x (This folder is guaranteed to always exist).
You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

The file system starts in the main folder, then the operations in logs are performed.

Return the minimum number of operations needed to go back to the main folder after the change folder operations.

 

Example 1:



Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2
Explanation: Use this change folder operation "../" 2 times and go back to the main folder."""
logs = ["d1/", "d2/", "../", "d21/", "./"]

# taking a directory stack i.e. the stack which will have the active directories
directory = []
# directory = [0] * len(logs)

for operation in logs:

    # if operation would'nt be '../' or './' then it means it's a directory
    # so, it will be pushed to the stack
    if operation != "../" and operation != "./":
        directory.append(operation)
    # if operation is "./" means do nothing, remain in the same directory
    # so, nothing will be pushed
    elif operation == "./":
        continue
    # if operation would be '../' so, directory in the top will be pushed
    # as we have to go to the directory previous to the directory on top of the stack
    else:
        if len(directory) >= 1:
            directory.pop()
print(directory)
print(len(directory))
