# 2つのリストをマージしたものを作成していく(マージソートの要領)
# O(m + n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        marged_list = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if (len(nums1) + len(nums2)) // 2 < i + j:
                break
            if nums1[i] <= nums2[j]:
                marged_list.append(nums1[i])
                i += 1
            else:
                marged_list.append(nums2[j])
                j += 1
        else:
            if len(nums1) <= i:
                marged_list += nums2[j : (len(nums1) + len(nums2)) // 2 - i + 1]
            else:
                marged_list += nums1[i : (len(nums1) + len(nums2)) // 2 - j + 1]

        if (len(nums1) + len(nums2)) % 2 == 1:
            return marged_list[-1]
        else:
            return (marged_list[-2] + marged_list[-1]) / 2


# 2分探索
# k番目に小さい要素を求める関数を作成
# 小さい方からk-1個を削除すればk番目に小さいものは求められる。
# nums1: [1, 4, 5, 7, 9] nums2: [2, 3, 6, 8]
# nums1[3]=5 > nums2[1]=3 なので、nums2[0], nums2[1]は中央値にならないから捨てる
# というように、小さい方からk-1個を削除していく
# O(log(min(m, n)))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # k=0のとき最小値を返す
        def get_kth_small(k, a_start, a_end, b_start, b_end):
            if a_start >= a_end:
                return nums2[k - a_start]
            if b_start >= b_end:
                return nums1[k - b_start]
            a_middle = (a_start + a_end) // 2
            b_middle = (b_start + b_end) // 2
            if a_middle + b_middle < k:
                if nums1[a_middle] < nums2[b_middle]:
                    return get_kth_small(k, a_middle + 1, a_end, b_start, b_end)
                return get_kth_small(k, a_start, a_end, b_middle + 1, b_end)
            if nums1[a_middle] < nums2[b_middle]:
                return get_kth_small(k, a_start, a_end, b_start, b_middle)
            return get_kth_small(k, a_start, a_middle, b_start, b_end)

        nums_length = len(nums1) + len(nums2)
        if nums_length % 2 == 1:
            return get_kth_small(nums_length // 2, 0, len(nums1), 0, len(nums2))
        return (
            get_kth_small(nums_length // 2 - 1, 0, len(nums1), 0, len(nums2))
            + get_kth_small(nums_length // 2, 0, len(nums1), 0, len(nums2))
        ) / 2
