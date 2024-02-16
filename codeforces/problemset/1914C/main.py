for _ in range(int(input())):
    _, r, w, l = map(int, input().split())
    t = map(int, input().split())
    i = 0

    for j in t:
        r -= min(l, j-1 - i) + 1
        i = j


    if r <= 0: print("NO")
    else: print("YES")
        