import csv # import csv module
import unicodedata2 # import unicodedata2 module


data = [] # liste vide

fichier_csv = 'conso-annuelles_v1.csv' # nom du fichier csv

outfile = open("conso-clean.csv", "w") # nom du fichier de sortie et mode d'ouverture (w = write)


with open(fichier_csv, 'r') as csvfile: # ouverture du fichier csv en mode lecture
    csvreader = csv.reader(csvfile, delimiter=';') # création d'un objet csvreader
    for row in csvreader: # boucle sur les lignes du fichier csv
        if row[0] != '' and row[1] != '' and row[2] != '' and row[3] != '' and row[4] != '': # Supprime les lignes vides
            data.append([
                row[0], # Appareil suivi
                row[1], # ID logement
                row[2], # Consommation annuelle AN1
                row[3], # Consommation annuelle AN2
                row[4], # Type
            ]) # ajout de la ligne dans la liste data

# supprimer id logement
for row in data:
    del row[1]

# remplace � par e
for row in data:
    row[0] = unicodedata2.normalize('NFKD', row[0]).encode('ascii', 'ignore').decode('utf-8')
    row[1] = unicodedata2.normalize('NFKD', row[1]).encode('ascii', 'ignore').decode('utf-8')
    row[2] = unicodedata2.normalize('NFKD', row[2]).encode('ascii', 'ignore').decode('utf-8')
    row[3] = unicodedata2.normalize('NFKD', row[3]).encode('ascii', 'ignore').decode('utf-8')

# remplace "i12" par "e"
for row in data:
    row[0] = row[0].replace('i12', 'e')
    row[1] = row[1].replace('i12', 'e')
    row[2] = row[2].replace('i12', 'e')
    row[3] = row[3].replace('i12', 'e')

# ENLEVER L'entete
data.pop(0)


# could not convert string to float '22,2'
# remplace "," par "."
for row in data:
    row[0] = row[0].replace(',', '.')
    row[1] = row[1].replace(',', '.')
    row[2] = row[2].replace(',', '.')
    row[3] = row[3].replace(',', '.')

# ValueError: could not convert string to float: '-'
# remplace "-" par "0"
for row in data:
    row[0] = row[0].replace('-', '0')
    row[1] = row[1].replace('-', '0')
    row[2] = row[2].replace('-', '0')
    row[3] = row[3].replace('-', '0')

# additionner les deux colonnes
for row in data:
    row[2] = float(row[2]) + float(row[1])
    del row[1]

# arrondir les valeurs
for row in data:
    row[1] = round(float(row[1]), 2)


# Trie par rapport au Type and Consommation annuelle ordre decroissant
data.sort(key=lambda x: (x[2], x[1]), reverse=True)




# tri par Type (colonne 3) ordre decroissant    
#data.sort(key=lambda x: x[2], reverse=True)
# ajouter le tri par consommation (colonne 2) ordre decroissant
#data.sort(key=lambda x: x[1], reverse=True)



# re ajouter l'entete
data.insert(0, ['Appareil suivi', 'Consommation annuelle AN1 + AN2', 'Type'])


    




with open('conso-clean.csv', 'w', newline='') as csvfile: # ouverture du fichier de sortie en mode écriture
    writer = csv.writer(csvfile, delimiter=';') # création d'un objet writer pour écrire dans le fichier de sortie
    writer.writerows(data)
    






#for d in data: # boucle sur les lignes de la liste data
   #outfile.write(d[0] + ';' + d[1] + ';' + d[2] + ';' + d[3] + ' \r  ') # écriture dans le fichier de sortie
       
# outfile.close()



















# outfile = open("conso-clean.csv", "w")  # Nom du fichier de sortie
  
# with open(fichier_csv, "r") as csv_file: # open the csv file
#    csv_reader = csv.reader(csv_file, delimiter=";") # read the csv file
    
#    for row in csv_reader: 
#        appareil_suivi = row[0]
#        id_logement = row[1]
#       conso_annuelle_ann1 = row[2]
#        conso_annuelle_ann2 = row[3]
#        type_or = row[4]
#
#        if not '' in row: # Enleve les lignes vides
#            line = "{},{},{},{}\n".format(appareil_suivi, conso_annuelle_ann1, conso_annuelle_ann2, type_or)
#            outfile.write(line)
#    outfile.close()













#def add_column_in_csv(input_file, output_file, transform_row):
    #""" Append a column in existing csv using csv.reader / csv.writer classes"""
    # Open the input_file in read mode and output_file in write mode
    #with open(input_file, 'r') as read_obj, \
            #open(output_file, 'w', newline='') as write_obj:
        # Create a csv.reader object from the input file object
        #csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        #csv_writer = writer(write_obj)
        # Read each row of the input csv file as list
        #for row in csv_reader:
            # Pass the list / row in the transform function to add column text for this row
         #   transform_row(row, csv_reader.line_num)
            # Write the updated row / list to the output file
          #  csv_writer.writerow(row) 



#header_of_new_col = 'Address'
#default_text = 'Some_Text'
#add_column_in_csv ('conso-annuelles_v1.csv', 'conso-clean.csv',
#                  lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(
#                      default_text))