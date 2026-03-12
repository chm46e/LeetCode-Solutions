1class Solution:
2    def addDigits(self, num: int) -> int:
3        num_str = str(num)
4        while len(num_str) > 1:
5            new_num = 0
6            for char in num_str:
7                new_num += int(char)
8            num_str = str(new_num)
9        return int(num_str)
10        