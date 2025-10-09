# Problem: Long Pressed Name - https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        stack1 = []

        for char in name:
            if not stack1 or stack1[-1][0] != char:
                stack1.append([char, 1])
            else:
                stack1[-1][1] += 1

        stack2 = []

        for char in typed:
            if not stack2 or stack2[-1][0] != char:
                stack2.append([char, 1])
            else:
                stack2[-1][1] += 1
        
        if len(stack2) == len(stack1):
            for i in range(len(stack2)):
                if not(stack2[i][0] == stack1[i][0] and stack2[i][1] >= stack1[i][1]):
                    return False
        else:
            return False
        return True

        