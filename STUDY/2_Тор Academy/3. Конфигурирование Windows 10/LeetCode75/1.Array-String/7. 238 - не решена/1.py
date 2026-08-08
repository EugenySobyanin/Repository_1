# 238. Product of Array Except Self
# medium
# наивное решение


from typing import List
from math import prod


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        
        for i in range(len(nums)):
            # передвигаем эл.т который не учитываем в произведениии в начало списка
            nums[0], nums[i] = nums[i], nums[0]
            # prod() - вычисляет произведение эл.тов в списке
            answer.append(prod(nums[1:]))
                
        return answer
    
    
obj = Solution()
print(obj.productExceptSelf([1, 2, 3, 4]))
print(obj.productExceptSelf([-1,1,0,-3,3]))