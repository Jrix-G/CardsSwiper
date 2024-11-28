def recherche_dicho(liste, e):
    left = 0
    right = len(liste) - 1
    while left <= right:
        mid = (left + right) // 2
        if liste[mid] < e:
            left = mid + 1
        elif liste[mid] > e:
            right = mid - 1
        else:
            return liste

    liste.append(0)
    for i in range(len(liste) - 1, left, -1):
        liste[i] = liste[i - 1]
    liste[left] = e
    return liste

import random
def list_creation(n):
    liste = []
    for i in range(n):
        liste.append(random.randint(0, 1000))
    return liste

import time
"""
start_time = time.time()
print(recherche_dicho(list_creation(1000000), 1000))
second_time = time.time()
print("Temps dicho", second_time - start_time)
"""

def test(liste):
    if len(liste) <= 1:
        return liste
    mid = len(liste) // 2
    left = test(liste[:mid])
    right = test(liste[mid:])
    return fusion(left, right)

def fusion(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])    
    return result


time_un = time.time()
print(test(list_creation(10**7)))
time_deux = time.time()
print("temps", time_deux - time_un)

