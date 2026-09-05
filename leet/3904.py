class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        suff = [0] * n
        suff[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suff[i] = min(suff[i + 1], nums[i])

        pref = nums[0]

        for i in range(n):
            pref = max(pref, nums[i])

            if pref - suff[i] <= k:
                return i

        return -1
