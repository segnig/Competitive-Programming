# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution(object):
    def printVertically(self, s):
        l = max([len(word) for word in s.split()])
        store = [[] for _ in range(l)]

        for word in s.split():
            for index in range(l):
                if index < len(word):
                    store[index].append(word[index])
                else:
                    store[index].append(" ")

        res = ["".join(chars) for chars in store]
        store = []

        for word in res:
            lenght = len(word) - 1
            while lenght and word[lenght] == " ":
                lenght -= 1
            store.append(word[:lenght + 1])

        return store