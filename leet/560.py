from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0
        seen = {0: 1}

        for i in nums:
            prefix = i + prefix
            need = prefix - k

            if need in seen:
                count += seen[need]
            seen[prefix] = seen.get(prefix, 0) + 1
        return count
