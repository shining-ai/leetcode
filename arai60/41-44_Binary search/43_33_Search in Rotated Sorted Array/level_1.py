def solve_1(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid
            else:
                right = mid - 1

    return -1


def solve_2(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1

    pivot = left

    if nums[pivot] <= target <= nums[-1]:
        left = pivot
        right = len(nums) - 1
    else:
        left = 0
        right = pivot - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    nums = [5, 1, 3]
    target = 3
    print(solve_1(nums, target))
    print(solve_2(nums, target))
