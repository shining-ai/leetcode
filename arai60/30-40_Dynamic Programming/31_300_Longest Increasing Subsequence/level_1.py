# O(n^2) time complexity
# O(n) space complexity
def solve_1(nums):
    subsequence_num = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                subsequence_num[i] = max(
                    subsequence_num[i], subsequence_num[j] + 1
                )

    return max(subsequence_num)


import bisect


def solve_2(nums):
    sub = [nums[0]]

    for i_num in nums:
        combo = bisect.bisect_left(sub, i_num)

        if combo >= len(sub):
            sub.append(i_num)

        if sub[combo] > i_num:
            sub[combo] = i_num

    return len(sub)


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(solve_1(nums))
    print(solve_2(nums))
