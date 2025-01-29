from sys import stdin

n, k = map(int, stdin.readline().split())

ans = 1
for i in range(2, n+1):
    ans = ((ans + k - 1) % i) + 1
    
print(ans)