def est_premier(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i <= n // i:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Exemple d'utilisation
nombre = 29
if est_premier(nombre):
    print(f"{nombre} est un nombre premier.")
else:
    print(f"{nombre} n'est pas un nombre premier.")