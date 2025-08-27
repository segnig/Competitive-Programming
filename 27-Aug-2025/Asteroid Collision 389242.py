# Problem: Asteroid Collision - https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            if not stack:
                stack.append(ast)
                continue
            explode = False

            while stack and ast < 0 and stack[-1] > 0 and stack[-1] < abs(ast):
                print("here")
                stack.pop()
            
            if stack and ast < 0 and stack[-1] > 0 and stack[-1] > abs(ast):
                continue


            if stack and ast < 0 and stack[-1] > 0 and stack[-1] == abs(ast):
                stack.pop()
            else:
                stack.append(ast)
            
            
        return stack