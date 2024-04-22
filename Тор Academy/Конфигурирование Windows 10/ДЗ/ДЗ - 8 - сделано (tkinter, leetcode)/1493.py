# 1493. Longest Subarray of 1's After Deleting One Element

from typing import List

# Наивное решение
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        lengths, current_section, max_result = [], 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current_section += 1
            else:
                lengths.append(current_section)
                current_section = 0
        if current_section:
            lengths.append(current_section)
        max_result = lengths[0]
        for i in range(1, len(lengths)):
            sum = lengths[i-1] + lengths[i]
            max_result = max(max_result, sum)
        return max_result - 1 if 0 not in nums else max_result
    

obj1 = Solution()
test1 = [1, 1, 0, 1]
test2 = [0, 1, 1, 1, 0, 1, 1, 0, 1]
test3 = [1, 1, 1]

print(obj1.longestSubarray(test1))
print(obj1.longestSubarray(test2))
print(obj1.longestSubarray(test3))