import csv # import de  la librairie csv
import pandas as pd # import de la librairie pandas

fichier_csv = "conso-annuelles_v1.csv" # nom du fichier csv

data = pd.read_csv(fichier_csv, sep=";") # lecture du fichier csv








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