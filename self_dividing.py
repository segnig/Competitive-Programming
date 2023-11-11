class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right + 1):
            T = True
            g = str(i)
            for j in g:
                if j == '0':
                    T = False
                elif i % int(j) != 0:
                    T = False
            if T:
                ans.append(i)

        return ans
