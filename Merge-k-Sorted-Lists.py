1import heapq
2
3# Definition for singly-linked list.
4# class ListNode:
5#     def __init__(self, val=0, next=None):
6#         self.val = val
7#         self.next = next
8class Solution:
9    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
10        pq = []
11        for linked_list in lists:
12            node = linked_list
13            while node:
14                heapq.heappush_max(pq, node.val)
15                node = node.next
16        last_node = None
17        while len(pq):
18            value = heapq.heappop_max(pq)
19            last_node = ListNode(value, last_node)
20        return last_node
21        