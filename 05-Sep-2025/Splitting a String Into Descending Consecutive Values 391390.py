# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        s += "0"
        n = len(s)
        e, i, cur_index, k, z = 0, 0, 1, 0, 0
        h = int(s)
        
        if n == 2 or h == 0:
            return False
        
        while cur_index < n - 1:
            num1 = int(s[e:i + 1])
            num2 = int(s[i + 1:cur_index + 1])
            
            k = num1 - num2
            if num1 == 0 and num2 == 0:
                k = 1
            
            if k == 1:
                if e == 0:
                    z = i
                e, i, cur_index = i + 1, cur_index, cur_index + 1
            elif k > 1 and cur_index != n - 2:
                cur_index += 1
            else:
                e, i, z, cur_index = 0, z + 1, z + 1, z + 2
        
        if k==1:
            return True
        else:
            return False