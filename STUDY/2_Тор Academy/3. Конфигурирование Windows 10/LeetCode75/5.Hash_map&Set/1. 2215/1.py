# 2215. Find the Difference of Two Arrays
# easy
# Первое наивное решение
# Решено Скорость - 29%, память - 5% 

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = [None] * 2
        result[0] = set(nums1).difference(set(nums2))
        result[1] = set(nums2).difference(set(nums1))
        return result
    
    
obj = Solution()
test1 = ([1, 2, 3, 4, 5, 6,], [4, 5, 6, 7, 8, 9])
print(obj.findDifference(*test1))