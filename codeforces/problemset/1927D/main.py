def printF(x, y): print("{} {}".format(x, y))
def search(inicio, fin):
    

for _ in range(int(input())):
    input()
    arr = list(map(int, input().split()))
    for _ in range(int(input())):
        i, j = map(lambda x: int(x)-1, input().split())
        tmp = i+1
        cut = False
        while (i < j):
            while (tmp <= j):
                if arr[i] != arr[tmp]:
                    printF(i+1, tmp+1)
                    cut = True;
                    break;
                tmp += 1

            if cut: break;
            i += 1

        if cut: continue;        
        printF(-1, -1)
