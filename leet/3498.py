class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0

        for index, value in enumerate(s):
            rever_index = 123 - ord(value)
            result += rever_index * (index + 1)
        return result
