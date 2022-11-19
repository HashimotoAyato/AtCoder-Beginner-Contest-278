H, M = map(int, input().split())

def check(H,M):
    h, m = str(H).zfill(2), str(M).zfill(2)
    if int(h[0])*10 + int(m[0]) < 24 and int(h[1])*10 + int(m[1]) < 60:
        return True
    else:
        return False

while True:
    if check(H,M):
        break
    else:
        M += 1
        if M == 60:
            M = 0
            H += 1
        if H == 24:
            H = 0

print(H,M)

