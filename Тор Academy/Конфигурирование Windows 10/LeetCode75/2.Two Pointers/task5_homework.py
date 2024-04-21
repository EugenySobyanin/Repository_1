# 11. Container With Most Water

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result, left, right = 0, 0, len(height) - 1
        while left <= right:
            current_value = (right - left) * min(height[left], height[right])
            result = max(current_value, result)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1    
        return result


test1 = Solution()
test1_list = [2, 3, 4, 5, 18, 17, 6]
print(test1.maxArea(test1_list))
