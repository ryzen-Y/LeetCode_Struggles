from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        first = 0
        second = 0
        for i in range(n):
            first += mat[i][i]
            second += mat[i][n-1-i]

        if n % 2 != 0:
            ans = (first + second) - mat[n // 2][n//2]
            return ans
        ans = first + second
        return ans
