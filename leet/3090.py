class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        seen = {}
        left = 0
        max_len = 0

        for i in range(len(s)):
            seen[s[i]] = seen.get(s[i], 0) + 1

            while seen[s[i]] > 2:
                seen[s[left]] -= 1
                left += 1
            max_len = max(max_len, (i - left) + 1)

        return max_len
