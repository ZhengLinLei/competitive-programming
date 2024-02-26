def rellenar(a):
    j = len(a)

    return "0"*(4-j)+a

while True:
    try:
        meses = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        p = 0
        d0, m0, y0, d1, m1, y1 = input().split()
        y0, y1 = rellenar(y0), rellenar(y1)

        if d0+m0+y0 == d1+m1+y1:
            mes = int(y0[1]+y0[0])
            dia = int(y0[3]+y0[2])
            if mes in range(1, 13) and dia in range(1, meses[int(mes)-1]+1):
                p += 1 

            print(p)
            continue

        # exchange
        if int(y1) < int(y0):
            y1, y0 = y0, y1
            m1, m0 = m0, m1
            d1, d0 = d0, d1
        elif int(y1) == int(y0):
            if int(m1) < int(m0):
                m1, m0 = m0, m1
                d1, d0 = d0, d1
            elif int(m1) == int(m0):
                d1, d0 = d0, d1

        #
        mes = int(y0[1]+y0[0])
        dia = int(y0[3]+y0[2])
        if y0 == y1:
            
            if mes in range(int(m0), int(m1)+1) and dia in range(int(d0), meses[int(mes)-1]+1):
                p += 1

            # Maximo 1
            print(p)
            continue
        else:
            #print(mes, dia)
            if mes in range(int(m0), 13) and dia in range(int(d0), meses[int(mes)-1]+1):
                p += 1

            for i in range(int(y0)+1, int(y1)):
                i = rellenar(str(i))
                mes = int(i[1]+i[0])
                dia = int(i[3]+i[2])
                if mes in range(1, 13) and dia in range(1, meses[int(mes)-1]+1):
                    p += 1 

            mes = int(y1[1]+y1[0])
            dia = int(y1[3]+y1[2])
            if mes in range(1, int(m1)+1) and dia in range(1, meses[int(mes)-1]+1):
                p += 1
            

            print(p)

    except:
        break