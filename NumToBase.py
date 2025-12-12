def StrToInt(Number):
    exp = len(Number) - 1
    ans = 0

    for i in Number:
        if i == "0":
            value = 0
        elif i == "1":
            value = 1
        elif i == "2":
            value = 2
        elif i == "3":
            value = 3
        elif i == "4":
            value = 4
        elif i == "5":
            value = 5
        elif i == "6":
            value = 6
        elif i == "7":
            value = 7
        elif i == "8":
            value = 8
        elif i == "9":
            value = 9
        ans = ans + (value * (10**exp))
        exp -= 1
    return ans

insert = (input("Enter your decimal number: "))
base = input("Enter the base you want to convert to: ")
base = StrToInt(base)
l = 0
j = []

if not insert.isdigit():
    print("You need to enter a positive decimal integer.")
elif base > 16 or base < 2:
    print("Base should be between 2 and 16")
else:
    insert = StrToInt(insert)
    if insert == 0:
        print("0")
    else:
        while insert != 0:
            mod = insert % base
            if mod != 0:
                if base < 10:
                    j+= str(mod)
                    insert = (insert-mod)//base
                elif 10 <= base <= 16:
                    if mod == 10:
                        j+= "A"
                    elif mod == 11:
                        j+= "B"
                    elif mod == 12:
                        j+= "C"
                    elif mod == 13:
                        j+= "D"
                    elif mod == 14:
                        j+= "E"
                    elif mod == 15:
                        j+= "F"
                    elif mod !=0:
                        j+= str(mod)
                    insert = (insert - mod) // base
            elif mod == 0:
                insert = insert//base
                j += "0"
        j = j[::-1]
        lj = len(j)
        n = 0
        ans = ""
        while n < lj:
            ans += j[n]
            n+=1
        print (ans)
