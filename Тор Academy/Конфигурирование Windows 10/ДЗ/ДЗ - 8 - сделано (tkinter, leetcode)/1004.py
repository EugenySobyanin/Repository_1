# 1004. Max Consecutive Ones III

from typing import List

# наивное решение
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_result = 0
        counter = 0
        for i in range(len(nums)):
            if nums[i] == 0 and k == 0:
                break
            if nums[i] == 0:
                k -= 1
            counter += 1
        max_result = max(max_result, counter)
        left = 0
        start = counter
        # print(f'Counter = {counter}')
        for i in range(start, len(nums)):
            if nums[i] == 1:
                counter += 1
                max_result = max(counter, max_result)
            elif nums[i] == 0 and nums[left] == 0:
                left += 1
                max_result = max(counter, max_result)
            elif nums[i] == 0 and nums[left] == 1:
                while nums[left] == 1:
                    left += 1
                    counter -= 1
                left += 1
                max_result = max(counter, max_result)
        return max_result
    

obj1 = Solution()
test1 = [0, 0, 0, 1, 1, 0, 0]
k1 = 3
test2 = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k2 = 2
test3 = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k3 = 3
test4 = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k4 = 3
test5 = [0, 0, 0, 1]
k5 = 4
test6 = [1, 0, 0, 0]
k6 = 2
print(obj1.longestOnes(test1, k1))
print(obj1.longestOnes(test2, k2))
print(obj1.longestOnes(test3, k3))
print(obj1.longestOnes(test4, k4))
print(obj1.longestOnes(test5, k5))
print(obj1.longestOnes(test6, k6))
        