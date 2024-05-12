# 1431. Kids With the Greatest Number of Candies
# easy
# понтовое решение
# хуже по скорости чем  перввое


from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [True if el + extraCandies >= max(candies) else False for el in candies]
    