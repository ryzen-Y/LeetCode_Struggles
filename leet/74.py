class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = matrix[mid]

                left = 0
                right = len(row) - 1

                while left <= right:
                    mid = (left + right) // 2

                    if row[mid] == target:
                        return True
                    elif row[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                return False

            elif target > matrix[mid][-1]:
                left = mid + 1
            else:
                right = mid - 1
        return False
