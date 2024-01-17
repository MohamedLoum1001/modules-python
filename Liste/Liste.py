personnes = ["Mohamed", "Ousmane", "Khadim", "Moukhtar"]
new_personne = "Abdou"

print("La liste des personnes avant ajout d'Abdou")
print(personnes)
print("La liste des personnes aprés ajout d'Abdou")

personnes.append(new_personne)
print(personnes)

# Supprimer une personne dans le tableau
del personnes[2]
print("La liste des personnes aprés avoir supprimé Khadim")
print(personnes)

# slice
# Syntaxe de slice : [start:stop:step]
# for i in personnes[0:3]:
#     print(i)