# 👉 EXERCICES DU 10/11/2023

# Fonction “multiplie” qui multiplie deux nombres en paramètre par additions successives.

def multiplie(a, b):
    resultat = 0
    i = 0
    while i < a:
        resultat += b
        i += 1
    return resultat
a = 5
b = 8
print(multiplie(a, b))

# Fonction “puissance” qui calcule les puissances par multiplication successives.

def puissance(c, d):
    resultat = 1
    i = 0
    while i < c:
        resultat *= d
        i += 1
    return resultat
c = 3
d = 8
print(puissance(c, d))


# 👉 EXERCICES DU 17/11/2023

# ➡️ Exercices Faciles

# Somme des nombres

def somme_des_nombres(n):
    somme = 0
    for nombre in range(1, n + 1):
        somme += nombre
    return somme
n = int(input("Entrez un nombre entier n : "))
resultat = somme_des_nombres(n)
print(f"La somme des nombres de 1 à {n} est : {resultat}")

# Table de Multiplication

def table_multiplication(n):
    i = 1
    while i <= 10:
        resultat = n * i
        print(f"{n} x {i} = {resultat}")
        i += 1
nombre_entier = int(input("Entrez un nombre entier : "))
table_multiplication(nombre_entier)

# Compteur Pair/Impair

def afficher_pair_impair():
    for nombre in range(1, 11):
        if nombre % 2 == 0:
            print(f"{nombre} est pair.")
        else:
            print(f"{nombre} est impair.")
afficher_pair_impair()

# ➡️ Exercices Intermédiaires

#Factorielle

def calcul_factorielle(n):
    resultat = 1
    while n > 1:
        resultat *= n
        n -= 1
    return resultat
nombre_entier = int(input("Entrez un nombre entier : "))
if nombre_entier < 0:
    print("La factorielle n'est pas définie pour les nombres négatifs.")
else:
    resultat_factorielle = calcul_factorielle(nombre_entier)
    print(f"La factorielle de {nombre_entier} est : {resultat_factorielle}")

#Palindrome

def palindrome(mot):
    return mot == mot[::-1]
mot_utilisateur = input("Entrez un mot : ")
if palindrome(mot_utilisateur):
    print(f"{mot_utilisateur} est un palindrome.")
else:
    print(f"{mot_utilisateur} n'est pas un palindrome.")

#Carré Magique

def generer_carre_magique(n):
    carre_magique = [[0] * n for _ in range(n)]
    i, j = 0, n // 2
    for num in range(1, n * n + 1):
        carre_magique[i][j] = num
        i -= 1
        j += 1
        if i < 0:
            i = n - 1
        if j == n:
            j = 0
        if carre_magique[i][j] != 0:
            i += 2
            j -= 1
            if i >= n:
                i -= n
            if j < 0:
                j = n - 1
    return carre_magique
def afficher_carre_magique(carre_magique):
    for ligne in carre_magique:
        print(" ".join(map(str, ligne)))
n = 3
carre_magique = generer_carre_magique(n)
afficher_carre_magique(carre_magique)
