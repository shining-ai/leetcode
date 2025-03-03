class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_element = []
        equal_element = []
        greater_element = []
        for num in nums:
            if num < pivot:
                less_element.append(num)
            elif num > pivot:
                greater_element.append(num)
            else:
                equal_element.append(num)

        nums = less_element + equal_element + greater_element
        return nums
