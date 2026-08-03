class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans = []
        sum_1 = 0
        for i in matrix:
            sum_1 = 0
            for j in i:
                sum_1 += j
            ans.append(sum_1)

        return ans
