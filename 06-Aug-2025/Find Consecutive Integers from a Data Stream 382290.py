# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.store = []
        self.k = k
        self.value = value
        

    def consec(self, num: int) -> bool: 
        if not self.store or self.store[-1][0] != num:
            self.store.append([num, 1])
        else:
            self.store[-1][1] += 1
        
        return False if not self.store else self.store[-1][1] >= self.k and self.store[-1][0] == self.value

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)