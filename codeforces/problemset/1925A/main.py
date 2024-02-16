t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    print(("".join([chr(i+97) for i in range(k)]))*n)
    