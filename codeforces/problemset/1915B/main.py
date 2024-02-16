for _ in range(int(input())):
    x = 0
    for i in range(3):
        x += sum(map(lambda s: ord(s) - 64 if s in ['A', 'B', 'C'] else 0, [*input()]))

    print(chr(64 + (18-x)))