# Problem: Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.size[rootX] < self.size[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
               
def main():
    n, m, k = map(int, input().split())
    uf = UnionFind(n)

    
    edges = set()
    
    for _ in range(m):
        u, v = map(int, input().split())
        u, v = u - 1, v - 1
        edges.add((u, v))
        edges.add((v, u))
        
        
    queries = []
       
    for _ in range(k):
        command, u, v = input().split()
        u, v = int(u) - 1, int(v) - 1
        
        if command == "cut":
            if (u, v) in edges:
                edges.remove((u, v))
                edges.remove((v, u))         
        queries.append((command, u, v))
        
    for edge in edges:
        u, v = edge
        uf.union(u, v)
        
    results = []
    for command, u, v in queries[::-1]:
        if command ==  "ask":
            if uf.find(u) == uf.find(v):
                results.append("YES")
            else:
                results.append("NO")
        else:
            uf.union(u, v)
        
    for result in results[::-1]:
        print(result)
                
            
if __name__ == "__main__":
    main()