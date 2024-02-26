while True:
    try:
        l = input().split(",")
        st = ""
        #print(l)
        
        for i in l:
            j = len(i)-1
            SED, SOD, SEP, SOP = 0, 0, 0, 0
            p = 1
            while j >= 0:
                num = int(i[j])

                if num % 2 == 0:
                    SED += num
                else:
                    SOD += num

                if p % 2 == 0:
                    SEP += num
                else:
                    SOP += num

                j -= 1
                p += 1

            if SED >= SOD and SEP <= SOP:
                st += "A"
            elif SED >= SOD and SEP > SOP:
                st += "T"
            elif SED < SOD and SEP >= SOP:
                st += "C"
            elif SED < SOD and SEP < SOP:
                st += "G"

        print(st)
    except EOFError:
        #print("ama")
        break