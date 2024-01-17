nom_chauffeur =    ["Mohamed", "Ousmane", "Khadim", "Moukhtar"]
distance_chauffeur_km = [1.5,    2.2,      0.2,     1.2]

index_min = 0
distance_min = distance_chauffeur_km[0]

for i in range(len(distance_chauffeur_km)):
    distance = distance_chauffeur_km[i]
    # Pour Trouver la chauffeur le plus proche
    if distance < distance_min:
    # Pour Trouver la chauffeur le plus loin
    # if distance > distance_min:   
        distance_min = distance
        index_min = i

print("La distance minimale: ", distance_min, "km")
print("Index de la distance minimale: ", index_min)
# print("Index de la distance maximale: ", index_min)
print("Nom du chauffeur : ", nom_chauffeur[index_min])