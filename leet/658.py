class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        record = []

        for value in arr:
            distance = abs(x - value)
            record.append((distance, value))

        record.sort()

        result = [value for distance, value in record[:k]]
        result.sort()

        return result
