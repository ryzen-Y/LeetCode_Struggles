class Solution:
    def validSequence(self, word1: str, word2: str):
        n = len(word1)
        m = len(word2)

       
        suf = [0] * (n + 1)

        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                suf[i] = suf[i + 1] + 1
                j -= 1
            else:
                suf[i] = suf[i + 1]

        ans = []
        j = 0
        mismatch = False

        for i in range(n):
            if j == m:
                break

            
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            
            elif not mismatch:
                
                if suf[i + 1] >= m - j - 1:
                    ans.append(i)
                    j += 1
                    mismatch = True

        if j == m:
            return ans

        return []