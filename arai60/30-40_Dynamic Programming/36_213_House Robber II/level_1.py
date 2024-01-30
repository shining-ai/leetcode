# O(n) time
# O(n) space
def solve_1(nums):
    house_num = len(nums)
    if house_num == 1:
        return nums[0]

    def rob_max(nums):
        house_num = len(nums)
        if house_num == 1:
            return nums[0]

        max_robbed_value = [0] * (house_num + 1)
        max_robbed_value[1] = nums[0]

        for i, i_money in enumerate(nums[1:], start=1):
            max_robbed_value[i + 1] = max(
                max_robbed_value[i],
                max_robbed_value[i - 1] + i_money,
            )

        return max_robbed_value[-1]

    max_value = max(
        rob_max(nums[:-1]),
        rob_max(nums[1:]),
    )

    return max_value


if __name__ == "__main__":
    nums = [2, 3, 2]
    print(solve_1(nums))
