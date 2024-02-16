for _ in range(int(input())):
    s, n = input(), map(int, input().split())
    z = 0
    m = 0
    for i in n:
        if i < 0: m += 1
        if i == 0: z+= 1
    if (z == 0) and (m % 2 == 0):
        print('1\n1 0')
    else:
        print('0')