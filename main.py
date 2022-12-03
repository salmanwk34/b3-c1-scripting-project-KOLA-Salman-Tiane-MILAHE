import csv # Importation du module csv
import unicodedata2 # importation de unicodedata2 pour la gestion des accents

data = [] # liste vide
fichier_csv = 'conso-annuelles_v1.csv' # nom du fichier csv
outfile = open("conso-clean.csv", "w") # nom du fichier de sortie et mode d'ouverture (w = write)

with open(fichier_csv, 'r') as csvfile: # ouverture du fichier csv en mode lecture
    csvreader = csv.reader(csvfile, delimiter=';') # création d'un objet csvreader
    for row in csvreader: # boucle sur les lignes du fichier csv
        if row[0] != '' and row[1] != '' and row[2] != '' and row[3] != '' and row[4] != '': # Supprime les lignes vides
            data.append([ # Ajoute les lignes dans la liste data
                row[0], # Appareil suivi
                row[1], # ID logement
                row[2], # Consommation annuelle AN1
                row[3], # Consommation annuelle AN2
                row[4], # Type
            ])
# supprimer id logement
for row in data:
    del row[1]

# remplace � par e (nettoyage des accents)
for row in data:
    row[0] = unicodedata2.normalize('NFKD', row[0]).encode('ascii', 'ignore').decode('utf-8')
    row[1] = unicodedata2.normalize('NFKD', row[1]).encode('ascii', 'ignore').decode('utf-8')
    row[2] = unicodedata2.normalize('NFKD', row[2]).encode('ascii', 'ignore').decode('utf-8')
    row[3] = unicodedata2.normalize('NFKD', row[3]).encode('ascii', 'ignore').decode('utf-8')

# remplace "i12" par "e" (confirmité)
for row in data:
    row[0] = row[0].replace('i12', 'e')
    row[1] = row[1].replace('i12', 'e')
    row[2] = row[2].replace('i12', 'e')
    row[3] = row[3].replace('i12', 'e')

# On enleve l'entete pour convertir
data.pop(0)

for row in data: # boucle sur les lignes du fichier csv
    row[0] = row[0].replace(',', '.') # remplace la virgule par un point
    row[1] = row[1].replace(',', '.') # remplace la virgule par un point
    row[2] = row[2].replace(',', '.') # remplace la virgule par un point
    row[3] = row[3].replace(',', '.') # remplace la virgule par un point

for row in data: # boucle sur les lignes du fichier csv
    row[0] = row[0].replace('-', '0') # remplace le tiret par un 0
    row[1] = row[1].replace('-', '0') # remplace le tiret par un 0
    row[2] = row[2].replace('-', '0') # remplace le tiret par un 0
    row[3] = row[3].replace('-', '0') # remplace le tiret par un 0

# Addition des deux colonnes
for row in data: 
    row[2] = float(row[2]) + float(row[1]) 
    del row[1] 

# On arrondie les valeurs
for row in data:
    row[1] = round(float(row[1]), 2)


# Tri par rapport au Type and Consommation annuelle ordre decroissant
data.sort(key=lambda x: (x[2], x[1]), reverse=True)

# re ajouter l'entete
data.insert(0, ['Appareil suivi', 'Consommation annuelle AN1 + AN2', 'Type']) 


with open('conso-clean.csv', 'w', newline='') as csvfile: # ouverture du fichier de sortie en mode écriture
    writer = csv.writer(csvfile, delimiter=';') # création d'un objet writer pour écrire dans le fichier de sortie
    writer.writerows(data) # écriture des lignes dans le fichier de sortie