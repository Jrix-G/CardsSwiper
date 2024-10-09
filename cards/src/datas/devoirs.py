l = int(input("Votre lettre"))
i = 97
j = 0
while l >= 1:
    k = 0
    while k <= j:
        print(chr(i), end=" ")
        k += 1
        i += 1
        if i == 123:
            i = 97
    print("")
    j += 1
    l -=1