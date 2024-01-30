def solve_1(nums):
    nums.sort()
    return nums[0]


def solve_2(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1

    return nums[left]


if __name__ == "__main__":
    nums = [4, 5, 1, 2, 3]
    print(solve_2(nums))
