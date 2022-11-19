N, Q = map(int, input().split())
follow = set()

for i in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        follow.add(','.join([str(A),str(B)]))
    if T == 2:
        follow.discard(','.join([str(A),str(B)]))
    if T == 3:
        if ','.join([str(A),str(B)]) in follow and ','.join([str(B),str(A)]) in follow:
            print('Yes')
        else:
            print('No')
