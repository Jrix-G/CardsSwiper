def estpremier(n):
    if n < 2:
        return False
    else:
        i = 2
        while i*i <= n:
            if n%i == 0:
                return False
            i += 1
    return True

print(estpremier(13))