#Programme qui demande à l'utilisateur un nombre entier N, puis calcule et affiche la factorielle de N en utilisant une boucle.

n = int(input("Entrez un nombre entier N : "))
factorielle = 1
for i in range(1, n + 1):
    factorielle *= i

print(f"La factorielle de {n} est : {factorielle}")
