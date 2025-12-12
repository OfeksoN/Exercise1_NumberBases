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

insert = input("Enter your binary number:")
digits = input("Enter Number of digits:")
digits = StrToInt(digits)
i = 0
if len(insert) > digits:
    print("The amount of digits should be higher then the length of the binary number")
elif not insert.isdigit():
    print("You need to enter a positive binary number.")
else:
    if len(insert) == digits:
        new = ""
        for i in insert:
            if i == "0":
                new =  new + "1"
            elif i == "1":
                new = new + "0"
    elif len(insert) < digits:
        n = digits-len(insert)
        insert = "0"*n + insert
        insert = str(insert)
        j=0
        new = ""
        for i in insert:
            if i == "0":
                new =  new + "1"
            elif i == "1":
                new = new + "0"
    index = digits-1
    newchar = ""
    new = list(new)
    n = -1
    for i in new[::-1]:
        if new[n] == "1":
            new[n] = "0"
            n = n-1
        elif new[n] == "0":
            new[n] = "1"
            break

    final = "".join(new)
    print(final)









