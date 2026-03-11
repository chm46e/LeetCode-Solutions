1class Solution:
2    def bitwiseComplement(self, n: int) -> int:
3        binary = bin(n)[2:]
4        result = ''
5
6        ignore = True
7        for bit in binary:
8            if ignore and bit == '1': # flipped
9                continue
10            elif ignore and bit == '0': # flipped
11                ignore = False
12            result += str(int(bit) ^ 1)
13        
14        if not result:
15            return 0
16        return int(result, 2)
17