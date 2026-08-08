# 1431. Kids With the Greatest Number of Candies
# easy
# первое решение (наивное)
# хорошо по скорости

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maximum_el = (max(candies))
        for el in candies:
            if el + extraCandies >= maximum_el:
                result.append(True)
                # maximum_el = el + extraCandies
            else:
                result.append(False)
        return result