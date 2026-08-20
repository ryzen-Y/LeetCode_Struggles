class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0

        for _ in range(k):
            if s[_] == 'a' or s[_] == 'e' or s[_] == 'i' or s[_] == 'o' or s[_] == 'u':
                count += 1

        i = 1
        j = k
        max_count = count

        while j < len(s):

            if s[i - 1] == 'a' or s[i - 1] == 'e' or s[i - 1] == 'i' or s[i - 1] == 'o' or s[i - 1] == 'u':
                count -= 1

            if s[j] == 'a' or s[j] == 'e' or s[j] == 'i' or s[j] == 'o' or s[j] == 'u':
                count += 1

            if count > max_count:
                max_count = count

            i += 1
            j += 1

        return max_count
