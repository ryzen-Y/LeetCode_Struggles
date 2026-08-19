from typing import List


class Solution:
    def merge(self, x: List[List[int]]) -> List[List[int]]:
        x.sort()
        merged = []

        start, end = x[0]

        for i in range(1, len(x)):
            next_start = x[i][0]
            next_end = x[i][1]

            if end >= next_start:
                end = max(end, next_end)
            else:
                merged.append([start, end])
                start = next_start
                end = next_end

        merged.append([start, end])

        return merged
