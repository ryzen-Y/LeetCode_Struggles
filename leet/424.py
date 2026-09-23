class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        window = {}
        maximum = 0

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            if (right - left + 1) - max(window.values()) > k:
                window[s[left]] -= 1
                left += 1
            maximum = max(maximum, right - left + 1)

        return maximum
