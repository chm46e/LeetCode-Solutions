1class MyCircularDeque:
2
3    def __init__(self, k: int):
4        self.deque = [0] * k
5        self.capacity = k
6        self.head = 0
7        self.tail = 0
8        self.size = 0
9        self.firstUse = True
10
11    def insertFront(self, value: int) -> bool:
12        if self.isFull():
13            return False
14
15        if not self.firstUse:
16            self.tail = (self.tail - 1) % self.capacity
17        else:
18            self.firstUse = False
19
20        self.deque[self.tail] = value
21        self.size += 1
22        return True
23
24    def insertLast(self, value: int) -> bool:
25        if self.isFull():
26            return False
27
28        if not self.firstUse:
29            self.head = (self.head + 1) % self.capacity
30        else:
31            self.firstUse = False
32        self.deque[self.head] = value
33        self.size += 1
34        return True
35
36    def deleteFront(self) -> bool:
37        if self.isEmpty():
38            return False
39
40        self.tail = (self.tail + 1) % self.capacity
41        self.size -= 1
42
43        if self.size <= 0:
44            self.size = 0
45            self.head = 0
46            self.tail = 0
47            self.firstUse = True
48        return True
49
50    def deleteLast(self) -> bool:
51        if self.isEmpty():
52            return False
53
54        self.head = (self.head - 1) % self.capacity
55        self.size -= 1
56
57        if self.size <= 0:
58            self.size = 0
59            self.head = 0
60            self.tail = 0
61            self.firstUse = True
62        return True
63
64    def getFront(self) -> int:
65        if self.isEmpty():
66            return -1
67        return self.deque[self.tail]
68
69    def getRear(self) -> int:
70        if self.isEmpty():
71            return -1
72        return self.deque[self.head]
73
74    def isEmpty(self) -> bool:
75        return self.size <= 0
76
77    def isFull(self) -> bool:
78        return self.size >= self.capacity
79
80
81# Your MyCircularDeque object will be instantiated and called as such:
82# obj = MyCircularDeque(k)
83# param_1 = obj.insertFront(value)
84# param_2 = obj.insertLast(value)
85# param_3 = obj.deleteFront()
86# param_4 = obj.deleteLast()
87# param_5 = obj.getFront()
88# param_6 = obj.getRear()
89# param_7 = obj.isEmpty()
90# param_8 = obj.isFull()