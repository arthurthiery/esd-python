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

#Programme qui génère et affiche un carré magique d'ordre N (N est un nombre impair) en utilisant une boucle.
