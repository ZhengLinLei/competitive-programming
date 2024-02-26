def printF(x, y): print("{} {}".format(x, y))
for _ in range(int(input())):
    input()
    arr = list(map(int, input().split()))
    for _ in range(int(input())):
        r = list(map(lambda x: int(x)-1, input().split()))
        i = min(r)
        j = max(r)
        cut = False
        for x in range(round((j-i)/2)+i + 1):
            if arr[i] != arr[j]:
                printF(i+1, j+1)
                cut = True
                break
                
            i += 1; j -= 1

        if not cut:
            printF(-1, -1)

    print()