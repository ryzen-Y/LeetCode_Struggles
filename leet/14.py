class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        s = strs[0]

        for i in range(1, len(strs)):
            word = strs[i]
            temp = ""
            n = min(len(s), len(word))

            for j in range(n):
                if s[j] == word[j]:
                    temp += s[j]
                else:
                    break

            s = temp

            if s == "":
                return ""

        return s
