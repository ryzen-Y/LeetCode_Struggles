from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        line = []
        line.append(0)

        for i in gain:
            ans += i
            line.append(ans)
        return max(line)
