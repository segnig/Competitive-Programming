class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        le = 0
        resu = ''
        while le < len(word1) and le < len(word2):
            resu = resu + word1[le]
            resu = resu + word2[le]
            le = le + 1
        if le != len(word1):
            resu = resu + word1[le:]
        if le != len(word2):
            resu = resu + word2[le:]
        return resu
