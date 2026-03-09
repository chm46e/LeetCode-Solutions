1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        last_seen = {}
4        best_length = 0
5        head = 0
6        tail = 0
7        for i in range(len(s)):
8            char = s[i]
9            if char in last_seen and (head > last_seen[char] >= tail):
10                tail = last_seen[char] + 1
11            head += 1
12            last_seen[char] = i
13            best_length = max(best_length, head - tail)
14        return best_length
15        