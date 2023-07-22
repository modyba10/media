import json

# Chemin vers le fichier JSON à ouvrir
fichier_json = "file.json"

# Ouvrir le fichier JSON en mode lecture
with open(fichier_json, "r") as fichier:
    # Charger le contenu du fichier JSON dans une variable (une liste de dictionnaires en général)
    liste_objets = json.load(fichier)

# Dictionnaire pour stocker les objets ayant le même "group" et le même "nom"
objets_doublons = {}

# Parcourir chaque objet dans la liste
for objet in liste_objets:
    nom = objet["name"]
    group = objet["group"]
    
    # Générer une clé unique pour chaque combinaison de "group" et "nom"
    cle = f"{group}_{nom}"
    
    # Ajouter l'objet à la liste correspondante pour la combinaison "group" et "nom"
    if cle in objets_doublons:
        objets_doublons[cle].append(objet)
    else:
        objets_doublons[cle] = [objet]

# Afficher uniquement les doublons (les groupes d'objets ayant le même "group" et le même "nom")
for cle, objets in objets_doublons.items():
    if len(objets) > 1:
        print(f"Combinaison 'group' et 'nom': {cle}")
        for objet in objets:
            print(objet)
        print()
