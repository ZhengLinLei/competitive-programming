while True:
    try:
        a, b, t0, t1 = map(int, input().split())
        tmp = 0
        for _ in range(99):
            tmp = a*t1 + b*t0
            t0 = t1
            t1 = tmp

        print(t1)
    except:
        break
