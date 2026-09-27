class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        record = []

        for value in arr:
            distance = abs(x - value)
            record.append((distance, value))

        record.sort()

        result = [value for distance, value in record[:k]]
        result.sort()

        return result
