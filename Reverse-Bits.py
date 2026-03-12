1class Solution:
2    def reverseBits(self, n: int) -> int:
3        binary = bin(n)[2:][::-1]
4        binary += ('0' * (32 - len(binary)))
5        return int(binary, 2)
6
7
8        