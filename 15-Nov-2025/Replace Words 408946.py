# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        result = []

        dictionary = set(dictionary)

        for word in sentence.split():
            
            for index, char in enumerate(word):
                if word[:index+1] in dictionary:
                    result.append(word[:index+1])
                    break
            else:
                result.append(word[:index+1])

        return " ".join(result)