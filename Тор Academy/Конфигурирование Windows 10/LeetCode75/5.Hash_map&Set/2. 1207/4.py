# 1207. Unique Number of Occurrences
# easy
# Решение с Leetcode которое хорошо работает по скорости(вроде оно должно было хорошо работать)
# решено: Скорость 30%, память 98 %


from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ = {}
        for i in arr:
            if i in occ:
                occ[i] += 1
            else:
                occ[i] = 1

        occ2 = set()
        for j in occ.values():
            if j in occ2:
                return False
            else:
                occ2.add(j)
        
        return True