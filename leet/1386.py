from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seen = {}

        for rows, seat in reservedSeats:
            if rows not in seen:
                seen[rows] = set()
            seen[rows].add(seat)

        answer = (n - len(seen)) * 2

        for seat in seen.values():

            left = not any(i in seat for i in [2, 3, 4, 5])
            middle = not any(i in seat for i in [4, 5, 6, 7])
            right = not any(i in seat for i in [6, 7, 8, 9])

            if left and right:
                answer += 2
            elif left or right or middle:
                answer += 1
        return answer
