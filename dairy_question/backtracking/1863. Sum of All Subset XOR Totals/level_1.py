# 素直に全ての部分集合を列挙して、XORを計算する
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []
        def make_subset(i, current):
            if i == len(nums):
                subsets.append(current[:])
                return
            
            make_subset(i + 1, current)
            current.append(nums[i])
            make_subset(i + 1, current)
            current.pop()
        
        make_subset(0, [])

        sum_xor = 0
        for subset in subsets:
            xor = 0
            for num in subset:
                xor ^= num
            sum_xor += xor
        return sum_xor