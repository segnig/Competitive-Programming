# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs[1:]:
            temp = ""

            for i in range(len(word)):
                if i == len(prefix) or prefix[i] != word[i]:
                    break
                temp += prefix[i]
            prefix = temp
        
        return prefix   