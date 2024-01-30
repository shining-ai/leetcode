from collections import defaultdict


# O(n * klogk) time complexity
# O(nk) space complexity
def solve_1(strs):
    hash_map = defaultdict(list)

    for i_str in strs:
        str_key = "".join(sorted(i_str))
        hash_map[str_key].append(i_str)

    return hash_map.values()


# O(n * k) time complexity
# O(nk) space complexity
def solve_2(strs):
    hash_map = defaultdict(list)

    for i_s in strs:
        count = [0] * 26
        for i_char in i_s:
            count[ord(i_char) - ord("a")] += 1
        hash_map[tuple(count)].append(i_s)

    return hash_map.values()


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solve_1(strs))
    print(solve_2(strs))
