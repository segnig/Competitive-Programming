# Problem: Union of Arrays with Duplicates - https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

class Solution:    
    def findUnion(self, a, b):
        union = set()
        
        for num in a + b:
            union.add(num)
            
        return list(union)