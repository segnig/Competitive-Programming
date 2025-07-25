# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        p_count = Counter(p)      
        substring_count = Counter( s[:len(p)])
        left = 0
        ans = []
        for right in range(len(p), len(s)):                    
            if substring_count == p_count:
                ans.append(left)
            
            substring_count[s[left]] -= 1
            substring_count[s[right]] += 1
            
            left +=1
        if substring_count == p_count:
            ans.append(left)        

        return ans