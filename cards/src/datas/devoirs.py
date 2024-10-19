l = int(input("Nombre de ligne?: "))
letter = "a"
for i in range(l):
    print(" " * i, end="")
    for j in range(l - i):
        if letter == "z":
            print("z", end=" ")
            letter = "a"
        else:
            print(letter, end=" ")
            letter = chr(ord(letter) + 1)
    print("")
