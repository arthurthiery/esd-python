# EXERCICES DU 10/11/2023

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


# EXERCICES DU 17/11/2023

#Exercices Faciles

# Somme des nombres

N = int(input("Entrez un nombre entier N : "))
somme = 0
for i in range(1, N + 1):
    somme += i
print(f"La somme des nombres de 1 à {N} est : {somme}")

# Table de Multiplication

N = int(input("Entrez un nombre entier N pour la table de multiplication : "))
print(f"Table de multiplication de {N} :")
for i in range(1, 11):
    resultat = N * i
    print(f"{N} x {i} = {resultat}")

# Compteur Pair/Impair

for nombre in range(1, 11):
    if nombre % 2 == 0:
        print(f"{nombre} est un nombre pair.")
    else:
        print(f"{nombre} est un nombre impair.")

#Exercices Intermédiaire

#Programme qui demande à l'utilisateur un nombre entier N, puis calcule et affiche la factorielle de N en utilisant une boucle.

n = int(input("Entrez un nombre entier N : "))
factorielle = 1
for i in range(1, n + 1):
    factorielle *= i
print(f"La factorielle de {n} est : {factorielle}")

#Programme qui vérifie si un mot saisi par l'utilisateur est un palindrome.

mot = input("Entrez un mot : ")
mot_inverse = ''.join(reversed(mot))
if mot == mot_inverse:
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
