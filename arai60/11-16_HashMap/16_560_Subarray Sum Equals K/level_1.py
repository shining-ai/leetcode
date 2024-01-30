import collections


# O(n^3)
def solve_1(nums, k):
    count = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if sum(nums[i : j + 1]) == k:
                count += 1
    return count


# O(n^2)
def solve_2(nums, k):
    sums = [0]
    temp = 0
    for i_num in nums:
        temp += i_num
        sums.append(temp)

    sums.reverse()
    ans = 0

    while sums:
        curr = sums.pop()
        for i_sum in sums:
            if curr + k == i_sum:
                ans += 1

    return ans


# O(n)
def solve_3(nums, k):
    ans = 0
    sums = collections.defaultdict(int)
    sums[0] = 1
    temp = 0
    for i_num in nums:
        temp += i_num
        ans += sums[temp - k]
        sums[temp] += 1
    return ans


if __name__ == "__main__":
    nums = [1, 1, 1, 1]
    k = 2
    print(solve_1(nums, k))
    print(solve_2(nums, k))
    print(solve_3(nums, k))
