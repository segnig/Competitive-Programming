# Problem:  Remove All Adjacent Duplicates in String II - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        '''
          " deeeeddbbcccbdaa"  k = 3
            
            [(a,2)]
            
            "ps", k = 2
          
        '''
        
        stack = []
        
        for char in s:
            if not stack:
                stack.append([char, 1])
            
            elif stack[-1] == [char, k-1]:
                stack.pop()
            elif stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
        
        result = ""
        for char, count in stack:
            result += char*count
        
        return result
                
            
            