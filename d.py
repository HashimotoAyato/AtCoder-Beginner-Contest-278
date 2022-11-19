N = int(input())
A = list(map(int, input().split()))
Q = int(input())
q = [list(map(int, input().split())) for i in range(Q)]
outputs = []

q.reverse() # start from end
last = False

def output(start_idx, target, ans):
    sum = 0
    #print('s={}'.format(start_idx))
    for j in range(start_idx, Q+1):
        if j == Q:
            ans.append(sum+A[target-1])
            return Q
        if q[j][0] == 3:
            end_idx = output(j+1, q[j][1], ans)
        if q[j][0] == 2 and q[j][1] == target:
            sum += q[j][2]
        if q[j][0] == 1:
            ans.append(sum+q[j][1])
            return j+1

i = 0
while i < Q:
    if q[i][0] == 3:
        ans = []
        i = output(i+1, q[i][1], ans)
        outputs += reversed(ans)
    else:
        i += 1
        continue

outputs.reverse()
for a in outputs:
    print(a)
