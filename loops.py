# Fonction “multiplie” qui multiplie deux nombres en paramètre par additions successives.

def multiplie(a, b):
    resultat = 0
    for i in range(a):
        resultat += b
    return resultat

a = 5
b = 8

print(multiplie(a, b))

# Fonction “puissance” qui calcule les puissances par multiplication successives.

def puissance(base, exposant):
    resultat = 1
    for i in range(exposant):
        resultat *= base
    return resultat

a = 3
b = 8
print(puissance(a, b))
