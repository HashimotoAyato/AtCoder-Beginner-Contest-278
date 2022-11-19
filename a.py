N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = []

for i in range(K,N):
    ans.append(str(A[i]))

for i in range(K):
    if i == N:
        break
    ans.append('0')

print(' '.join(ans))