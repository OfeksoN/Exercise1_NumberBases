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

insert = (input("Enter your number: ").lower())
base = input("Enter the base you want to convert from: ")
exp = len(insert)-1
number = 0
value = 0
base = StrToInt(base)
if "-" in insert:
    print("Number has to be positive")
elif not all(ch in "0123456789abcdefABCDEF" for ch in insert):
    print("Invalid hexadecimal string.")
elif base > 1 and base <= 10 and not insert.isdigit():
    print("This base doesn't match the number you entered.")
else:
    for i in insert:
        if base > 10 and base <= 16:
            if i == "a" and 11 <= base <= 16:
                value = 10
            elif "a" in insert and base < 11:
                print("A and Letters above it doesn't belong to that base")
                break
            elif i == "b" and 12 <= base <= 16:
                value = 11
            elif "b" in insert and base < 12:
                print("B and Letters above it doesn't belong to that base")
                break
            elif i == "c" and 13 <= base <= 16:
                value = 12
            elif "c" in insert and base < 13:
                print("C and Letters above it doesn't belong to that base")
                break
            elif i == "d" and 14 <= base <= 16:
                value = 13
            elif "d" in insert and base < 14:
                print("D and Letters above it doesn't belong to that base")
                break
            elif i == "e" and 15 <= base <= 16:
                value = 14
            elif "e" in insert and base < 15:
                print("E and Letters above it doesn't belong to that base")
                break
            elif i == "f" and base == 16:
                value = 15
            elif "f" in insert and base < 16:
                print("F doesn't belong to that base")
                break
            elif "0" <= i <= "9":
                value = StrToInt(i)
            number = number + (value * (base**exp))
            exp -= 1
        elif base > 1 and base <= 10:
            if "0" <= i <= "9":
                value = StrToInt(i)
            number = number + (value * (base**exp))
            exp -= 1
    n = len(insert)
    j = 0
    if base < 2 or base > 16:
        print("Base should be between 2 and 16")
    elif insert == "0":
            print("0")
    elif 2 <= base and base < 10:
        for i in insert:
            if StrToInt(i) >= base and base < 10:
                print("The number that you entered can't contain a value which is equal or above the base")
                break
        else:
            print(number)
    else:
        print (number)