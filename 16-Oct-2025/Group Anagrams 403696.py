# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)

        for word in strs:
            counter = [0]*26
            for char in word:
                idx = ord(char) - ord("a")
                counter[idx] += 1

            store[tuple(counter)].append(word)

        return list(store.values())