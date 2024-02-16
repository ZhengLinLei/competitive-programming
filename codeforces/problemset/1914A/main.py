for _ in range(int(input())):
    input()
    log, r = {}, 0
    for i in [*input()]:
        log[i] = log[i] + 1 if i in log else 1

    for i in log:
        if log[i] >= (ord(i)-64): r += 1

    print(r)