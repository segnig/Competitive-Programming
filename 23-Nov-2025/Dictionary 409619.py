# Problem: Dictionary - https://codeforces.com/problemset/problem/1674/B

for _ in range(int(input())):
    word = input()

    a = ord(word[0]) - ord("a")

    b = ord(word[1]) - ord("a")
    result = a * 25 + b
    if word[0] > word[1]:
        result += 1
    
    print(result)