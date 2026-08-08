# 2215. Find the Difference of Two Arrays
# easy
# Ищем вариант улучшить первое решение
# Решено: 90% по скорости, 24% по памяти


from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        tmp = nums1
        nums1 = set(nums1).difference(nums2)
        nums2 = set(nums2).difference(tmp)
        return nums1, nums2
        
    
    
obj = Solution()
test1 = ([1, 2, 3, 4, 5, 6, 1], [4, 5, 6, 7, 8, 9])
print(obj.findDifference(*test1))        
        


