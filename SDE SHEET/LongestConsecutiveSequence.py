nums = [100, 4, 200, 1, 3, 2]


# initializations
n = len(nums)
nums.sort()
final_list = []


def check_base_cases(n, nums):
    if n == 0:
        return 0
    elif n == 1 or len(set(nums)) == 1:
        return 1


if check_base_cases(n, nums) != 1 and check_base_cases(n, nums) != 0:
    for i in range(n):
        if nums[i - 1] != nums[i]:
            if i == 0:
                final_list.append([nums[i]])
            else:
                if abs(nums[i] - nums[i - 1]) == 1:
                    final_list[-1].append(nums[i])
                else:
                    final_list.append([nums[i]])
    print(len(max(final_list, key=len)))
else:
    print(check_base_cases(n, nums))

"""Simple solution"""

n = len(nums)
nums.sort()

curr_seq, longest_seq = 1, 1

if n == 0:
    print(0)
else:
    for i in range(n):
        if nums[i - 1] != nums[i]:
            if abs(nums[i] - nums[i - 1]) == 1:
                curr_seq += 1
            else:
                longest_seq = max(longest_seq, curr_seq)
                curr_seq = 1
    print(max(longest_seq, curr_seq))
