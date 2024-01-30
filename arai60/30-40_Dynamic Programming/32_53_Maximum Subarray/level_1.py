import bisect


def solve_1(nums):
    max_sum = [nums[0]]

    for i_num in nums[1:]:
        max_sum.append(max(max_sum[-1] + i_num, i_num))

    return max(max_sum)


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solve_1(nums))
