# 2215. Find the Difference of Two Arrays
# easy
# Смотрим пример решения которое лучше работает по памяти
# 19 по скороти, 97 по памяти


from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        diff1=[i for i in set(nums1) if i not in nums2]
        diff2=[i for i in set(nums2) if i not in nums1]

        return [diff1, diff2]
    
    
obj = Solution()
test1 = ([1, 2, 3, 4, 5, 6, 1], [4, 5, 6, 7, 8, 9])
print(obj.findDifference(*test1)) 