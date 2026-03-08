1class Solution:
2    def findDifferentBinaryString(self, nums: List[str]) -> str:
3        unique = ""
4        for i in range(len(nums)):
5            num = nums[i]
6            bit = int(num[i])
7            unique += str(bit ^ 1)
8        return unique
9        