# Problem: Design Circular Queue - https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:

    def __init__(self, k: int):
        self.store = deque()
        self.capacity = k
        self.queue = deque()
        

    def enQueue(self, value: int) -> bool:
        if len(self.store) < self.capacity:
            self.store.append(value)
            return True
        self.queue.append(value)
        return False

    def deQueue(self) -> bool:
        if self.store:
            self.store.popleft()
            return True
        if self.queue:
            self.store.append(self.queue.popleft())
        return False
        

    def Front(self) -> int:
        if self.store:
            return self.store[0]
        return -1
        

    def Rear(self) -> int:
        if self.store:
            return self.store[-1]
        return -1

    def isEmpty(self) -> bool:
        return  len(self.store) == 0

    def isFull(self) -> bool:
        return len(self.store) == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()