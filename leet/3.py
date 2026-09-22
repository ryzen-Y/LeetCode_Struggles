class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        maximum = 0
        current = set()

        for i in range(len(s)):

            while s[i] in current:
                current.remove(s[left])
                left += 1
            current.add(s[i])
            maximum = max(maximum, len(current))
        return maximum


# sliding window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maximum = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            maximum = max(maximum, right - left + 1)
        return maximum
