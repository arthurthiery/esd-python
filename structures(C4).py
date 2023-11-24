#COURS DU 24/11 (partie 1)


# Exercie 1
ma_liste = [5, 3, 9, 1, 6]

ma_liste.append(7)
ma_liste.append(2)

ma_liste.sort()

print(ma_liste)


# Exercie 2
personne = {
    "nom": "Arthur Thiery",
    "âge": 20,
    "adresse": "24 Rue Jean Hameau, 33300 Bordeaux"
}

print(personne)


# Exercie 3
ensemble1 = {1, 2, 3, 4, 5}
ensemble2 = {4, 5, 6, 7, 8}

union = ensemble1.union(ensemble2)

intersection = ensemble1.intersection(ensemble2)

print("Union :", union)
print("Intersection :", intersection)
