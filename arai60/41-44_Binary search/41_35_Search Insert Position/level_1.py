import bisect


# ライブラリを使用
def solve_1(nums, target):
    ans = bisect.bisect_left(nums, target)
    return ans


def solve_2(nums, target):
    left = 0
    right = len(nums)

    while left < right:
        mid = (left + right) // 2
        if nums[left] < target:
            left = mid + 1
        else:
            right = mid

    return left


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 7
    print(solve_1(nums, target))
    print(solve_2(nums, target))
