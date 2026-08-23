class Solution:
    def sumGame(self, num: str) -> bool:

        count = 0
        first_sum = 0
        second_sum = 0
        n = len(num)
        q1 = 0
        q2 = 0

        for i in range(n//2):
            if num[i] == '?':
                q1 += 1
            else:
                first_sum += int(num[i])
        for i in range(n//2, n):
            if num[i] == '?':
                q2 += 1
            else:
                second_sum += int(num[i])

        return 2*(first_sum - second_sum) + 9*(q1-q2) != 0
