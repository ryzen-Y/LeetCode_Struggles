from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        sum = 0

        for _ in range(k):
            sum += arr[_]

        if sum / k >= threshold:
            count += 1

        i = 1
        j = k

        while (j < len(arr)):
            sum = sum + arr[j] - arr[i-1]
            if sum / k >= threshold:
                count += 1
            i += 1
            j += 1

        return count
