class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7

        def calc_prime_score(num):
            primes = []
            for prime in range(2, int(math.sqrt(num)) + 1):
                if num % prime != 0:
                    continue
                primes.append(prime)
                while num % prime == 0:
                    num //= prime
            if num >= 2:
                primes.append(num)
            return len(primes)

        prime_scores = [calc_prime_score(num) for num in nums]
        next_dominant = [len(nums)] * len(nums)
        prev_dominant = [-1] * len(nums)

        # subarrayの左側と右側のindexを保存
        stack = []
        for i, score in enumerate(prime_scores):
            while stack and prime_scores[stack[-1]] < score:
                top = stack.pop()
                next_dominant[top] = i
            if stack:
                prev_dominant[i] = stack[-1]
            stack.append(i)

        num_of_subarrays = [0] * len(nums)
        for index in range(len(nums)):
            num_of_subarrays[index] = (
                next_dominant[index] - index) * (
                index - prev_dominant[index])

        score_heap = []
        # 大きい順に取り出すために-1をかけている
        for index in range(len(nums)):
            heapq.heappush(score_heap, (-nums[index], index))

        score = 1

        # 高速に累乗のMODの剰余を求める
        def _power(base, exponent):
            res = 1
            while exponent > 0:
                if exponent % 2 == 1:
                    res = (res * base) % MOD
                base = (base * base) % MOD
                exponent //= 2
            return res

        while k > 0:
            num, index = heapq.heappop(score_heap)
            num = -num
            operations = min(k, num_of_subarrays[index])
            score = (score * _power(num, operations)) % MOD
            k -= operations

        return score
