class Solution:
    def uniformArray(self, num1: list[int]) -> bool:

        if num1[0] % 2 != 0:
            flag = True
            for i in range(len(num1)):
                if i == 0:
                    continue

                if num1[i] % 2 == 0:
                    found = False
                    for j in range(len(num1)):
                        if i != j:
                            diff = num1[i] - num1[j]
                            if diff % 2 == 1 and diff >= 1:
                                found = True
                                break
                    if found == False:
                        flag = False
            return flag

        else:
            flag = True
            for i in range(len(num1)):
                if i == 0:
                    continue

                if num1[i] % 2 != 0:
                    found = False
                    for j in range(len(num1)):
                        if i != j:
                            diff = num1[i] - num1[j]
                            if diff % 2 == 1 and diff >= 1:
                                found = True
                                break
                    if found == False:
                        flag = False
            return flag
