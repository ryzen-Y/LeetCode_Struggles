class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        s = ""

        for i in range(n):
            s = s + word1[i] + word2[i]

        if len(word1) > len(word2):
            s = s + word1[n:]
        else:
            s = s + word2[n:]

        return s
