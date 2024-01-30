import collections


def solve_1(s):
    hash_map = collections.defaultdict(int)

    for i_s in s:
        hash_map[i_s] += 1

    for i, i_s in enumerate(s):
        if hash_map[i_s] == 1:
            return i

    return -1


if __name__ == "__main__":
    s = "loveleetcode"
    print(solve_1(s))
