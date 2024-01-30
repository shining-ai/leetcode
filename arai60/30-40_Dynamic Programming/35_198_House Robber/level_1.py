# O(n) time
# O(n) space
def solve_1(nums):
    n = len(nums)

    if n == 1:
        return nums[0]

    max_robbed_value = [0] * (n + 1)
    max_robbed_value[1] = nums[0]

    for i, i_money in enumerate(nums[1:], start=2):
        max_robbed_value[i] = max(
            max_robbed_value[i - 1], max_robbed_value[i - 2] + i_money
        )

    return max_robbed_value[-1]


# O(n) time
# O(1) space
def solve_2(nums):
    n = len(nums)

    if n == 1:
        return nums[0]

    max_robbed_prev = nums[0]
    max_robbed_prev_prev = 0
    max_robbed_curr = 0

    for i_money in nums[1:]:
        max_robbed_curr = max(max_robbed_prev, max_robbed_prev_prev + i_money)
        max_robbed_prev_prev = max_robbed_prev
        max_robbed_prev = max_robbed_curr

    return max_robbed_curr


if __name__ == "__main__":
    nums = [1, 3, 1, 3, 100]
    print(solve_1(nums))
    print(solve_2(nums))
