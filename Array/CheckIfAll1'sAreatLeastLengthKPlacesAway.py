# nums = [1, 0, 0, 1, 0, 1]


nums = [1, 0, 0, 0, 1, 0, 0, 1]
k = 2


def find_k_dist(nums, k):
    dist = []
    for i in range(len(nums)):
        if nums[i] == 1:
            dist.append(i)
    print(dist)
    for i in range(len(dist) - 1):
        print(dist[i + 1] - dist[i] - 1)
        if dist[i + 1] - dist[i] - 1 < k:
            print(dist[i + 1] - dist[i] - 1)
            return False
    return True


print(find_k_dist(nums, k))
