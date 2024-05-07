# 1071 Greatest Common Divisor of Strings
# easy
# наивное решение

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        min_str = str1 if len(str1) < len(str2) else str2
        max_str = str2 if len(str2) > len(str1) else str1
        num = len(max_str) / len(min_str)
        if max_str == (min_str * int(num)):
            return min_str
        return ''

    
obj = Solution()
print(obj.gcdOfStrings("ABABAB", "AB"))
        