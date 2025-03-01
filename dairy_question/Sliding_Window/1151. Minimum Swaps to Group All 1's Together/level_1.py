class Solution:
    def minSwaps(self, data: List[int]) -> int:
        num_one = 0
        for num in data:
            if num == 1:
                num_one += 1
        left = 0
        right = num_one
        num_one_left_to_right = 0
        for i in range(left, right):
            if data[i] == 1:
                num_one_left_to_right += 1
        min_num_operation = num_one - num_one_left_to_right
        while right < len(data):
            if data[left] == 1:
                num_one_left_to_right -= 1
            if data[right] == 1:
                num_one_left_to_right += 1
            num_operation = num_one - num_one_left_to_right
            min_num_operation = min(min_num_operation, num_operation)
            left += 1
            right += 1

        return min_num_operation
