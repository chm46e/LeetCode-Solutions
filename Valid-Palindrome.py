1import re
2
3class Solution:
4    def isPalindrome(self, s: str) -> bool:
5        converted = s.lower()
6        converted = re.sub(r'[^a-z0-9]', "", converted)
7
8        if not converted or len(converted) == 1:
9            return True
10
11        left = 0
12        right = len(converted) - 1
13        while left < right:
14            if converted[left] != converted[right]:
15                return False
16            left += 1
17            right -= 1
18        return True
19
20