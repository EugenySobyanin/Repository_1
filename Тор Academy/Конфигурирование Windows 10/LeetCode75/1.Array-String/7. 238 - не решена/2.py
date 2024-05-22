# 238. Product of Array Except Self
# medium
# доработка первого решения
# добавлена оптимизация массивов с нулями
# все равно не прооходит по времени тест (большой массив с 1, -1)
# не решено


from typing import List
from math import prod


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        zero_in_nums = 0 in nums
        
        for i in range(len(nums)):
            
            if nums[i] != 0 and zero_in_nums:
                answer.append(0)
            else:
                nums[0], nums[i] = nums[i], nums[0]
                answer.append(prod(nums[1:]))
      
        return answer
    
    
obj = Solution()
print(obj.productExceptSelf([1, 2, 3, 4]))
print(obj.productExceptSelf([-1, 1, 0, -3, 3]))