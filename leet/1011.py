class Solution:
    def shipWithinDays(self, w: list[int], days: int) -> int:
        left = max(w)
        right = sum(w)
        result = right

        def checkcap(mid):
            ship = 1
            cap = mid

            for i in w:
                if cap - i < 0:
                    ship += 1
                    cap = mid
                cap = cap - i

            return ship <= days

        while left <= right:
            mid = (left + right) // 2

            if checkcap(mid):
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1

        return result
