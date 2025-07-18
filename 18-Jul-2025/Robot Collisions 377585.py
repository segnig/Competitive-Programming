# Problem: Robot Collisions - https://leetcode.com/problems/robot-collisions/

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = [[positions[i], healths[i], directions[i], i] for i in range(len(positions))]
        robots.sort()

        stack = []
        for robot in robots:
            if not stack or robot[2] == "R":
                stack.append(robot)
            else:
                online = True
                while stack and stack[-1][2] != robot[2]:
                    if stack[-1][1] == robot[1]:
                        stack.pop()
                        online = False
                        break
                    elif stack[-1][1] > robot[1]:
                        stack[-1][1] -= 1
                        online = False
                        break
                    else:
                        stack.pop()
                        robot[1] -= 1
                if online:
                    stack.append(robot)
        if not stack:
            return []
        stack.sort(key=lambda x: x[-1])
        return [x[1] for x in stack]