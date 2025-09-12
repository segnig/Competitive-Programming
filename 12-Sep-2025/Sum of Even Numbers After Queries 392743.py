# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_off_even_nums = 0

        for num in nums:
            if num % 2 == 0:
                sum_off_even_nums += num

        answer = []
        for i in range(len(queries)):
            if nums[queries[i][1]] % 2 == 0 and queries[i][0] % 2 == 0:
                sum_off_even_nums += queries[i][0]
            elif nums[queries[i][1]] % 2 == 0 and queries[i][0] % 2 != 0:
                sum_off_even_nums -= nums[queries[i][1]]
            
            elif nums[queries[i][1]] % 2 != 0 and queries[i][0] % 2 != 0:
                sum_off_even_nums += nums[queries[i][1]] + queries[i][0]
            
            nums[queries[i][1]] += queries[i][0]
            answer.append(sum_off_even_nums)
        
        return answer