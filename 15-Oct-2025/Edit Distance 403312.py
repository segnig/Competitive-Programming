# Problem: Edit Distance - https://leetcode.com/problems/edit-distance/description/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # base case "" == "" 0
        
        
        @cache
        def dp(i, j):
            if len(word1) == i and len(word2) == j:
                return 0
            if len(word1) == i:
                return len(word2) - j
                
            if len(word2) == j:
                return len(word1) - i 
            
            if word1[i] != word2[j]:
                delete = 1 + dp(i+1, j)
                insert = 1 + dp(i, j+1)
                replace = 1 + dp(i+1, j+1)
                
                return min([delete, insert, replace])
            
            return dp(i+1, j+1)
            
        return dp(0, 0)
        
        """
        horse
        ros
        (i1, i2)
        
        if 
        (i1, i2+1) + 1 => insert
        (i1+1, i2) + 1 => Delete
        (i1+1, i2 + 1) + 1 => replace
        
        
        
        """
        
        
        
        '''
            rorse
            ros..   
            
            3
            
            word1 = "intention", word2 = "execution"
            intention -> entention
            entention -> extention
            extention -> exention
            exention -> exection
            exection -> execution
            
            
            intention
            execution
            
        '''