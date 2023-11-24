#COURS DU 24/11 (partie 2)

#Gestionnaire de Contacts

contacts = {}

def ajouter_contact(nom, numero):
    contacts[nom] = numero

def supprimer_contact(nom):
    if nom in contacts:
        del contacts[nom]

def rechercher_contact(nom):
    return contacts.get(nom, "Contact non trouvé")

ajouter_contact("Arthur", "06 52 95 09 95")
print(rechercher_contact("Arthur"))
supprimer_contact("Arthur")
print(rechercher_contact("Arthur"))

#Convertisseur Température

def convertir_temperature(temp, de, vers):
    if de == "Celsius" and vers == "Fahrenheit":
        return temp * 9/5 + 32
    elif de == "Fahrenheit" and vers == "Celsius":
        return (temp - 32) * 5/9

print(convertir_temperature(20, "Celsius", "Fahrenheit"))

#Calculateur d’IMC

def calculer_imc(poids, taille):
    return poids / (taille ** 2)

print(calculer_imc(65, 1.80))

#Tri de Liste

def trier_liste(liste):
    nouvelle_liste = []
    while liste:
        minimum = liste[0]
        for x in liste: 
            if x < minimum:
                minimum = x
        nouvelle_liste.append(minimum)
        liste.remove(minimum)
    return nouvelle_liste

print(trier_liste([5, 2, 3, 1, 4]))
