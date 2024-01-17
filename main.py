# Collection en programmation = c'est les tableaux, listes & tuples... elle nous permet de contenir plusieurs éléments

# Exercice :  Demander les noms de personnes 
# boucle infinie, sort quand le nom vide on utilise un break

noms = []

# while True = boucle infini
while True: 
    nom = input("Nom de la personne : ")
    if nom == "":
        break
    # ajouter un nom sur la liste 
    noms.append(nom)

print()
print("Noms des personnes :")
# Trier par ordre alphabétique
noms.sort()
print(noms)