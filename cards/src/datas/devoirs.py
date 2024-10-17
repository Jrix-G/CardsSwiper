def reverse():
    n = input("Votre noms")
    word = ""
    for i in range(len(n)):
        word += n[-1-i]
    return n

def space_delete():
    n = input("Votre phrase")
    word = ""
    for i in range(len(n)):
        if n[i] != " ":
            word += n[i]
    return word

def convert(a, b, c):
    return a//60==b and (a-(a//60)*60 == c)

def inclus(n, b, c):
    return 10**(b-1) <= n < 10**(c)

#Or 
def incluss(n, b, c):
    number = 1
    i = 10
    while n//i != 0:
        number += 1
        i += i**2
    return(b <= n < c)

def small(s, s1, s2):
    return len(s1) == 1 and s1 != ("A" <= s1 <= "Z") and len(s2) == 1 and s2 != ("a" <= s <= "z") and s1+s2 in s or s2+s1 in s

def facto(n):
    if n <= 2:
        return 2
    else:
        for i in range(2, n):
            n *= i
    return n

def regle(n, x):
    print("|", end="")
    b = 1
    for i in range(n):
        print("-", end="")
        if b == x:
            print("|", end="")
            b = 0
        b += 1


def word():
    n = input("Word")
    mot = input("Word")
    while mot[0] != n:
        mot = input("Wordddd")
    print(mot)
