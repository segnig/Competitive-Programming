# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        word_counter = Counter(word)
        word_counter = list(word_counter.items())
        word_counter.sort(key=lambda x: x[1], reverse=True)
        result = 0
        for i, count in enumerate(word_counter):
            result += count[1] * ((i // 8) + 1)

        return result