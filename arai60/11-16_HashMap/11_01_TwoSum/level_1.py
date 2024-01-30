# O(N)
def two_pass_hashmap(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i

    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in hashmap and hashmap[difference] != i:
            return [i, hashmap[difference]]


# O(N)
def one_pass_hashmap(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in hashmap:
            return [hashmap[difference], i]

        hashmap[nums[i]] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    # two_pass_hashmap(nums, target)
    one_pass_hashmap(nums, target)
