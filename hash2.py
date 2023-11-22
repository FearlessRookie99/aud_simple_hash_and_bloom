import csv
import matplotlib.pyplot as plt

input_file  = 'da_DK.csv'
hashed_rows = 100000
hash_table_size = 100003  # Verwendet eine Primzahl für die Größe der Hash-Tabelle
hash_table = [None] * hash_table_size
hash_values = []

def h2(key):
    a = 79194
    b=  87931
    multiplication_constant = 0.61803398875  # Ein typischer Wert für die Multiplikation
    hash_value = 0

    for char in key:
        # Division
        hash_value = (hash_value * a + ord(char)+b) % hash_table_size

    # Multiplikation
    hash_value = int(hash_value * multiplication_constant * hash_table_size) % hash_table_size

    hash_values.append(hash_value)

    return hash_value


# Öffnen und Lesen der CSV-Datei und Einlesen der ersten 100.000 Werte
input_data = []

with open(input_file, 'r', newline='',encoding='utf-8') as infile:
    reader = csv.reader(infile)
    row_count = 0
    for row in reader:
        # hier eingeben wie viele Zeilen 
        if row_count >= hashed_rows:
            break
        if len(row) > 0:
            input_data.append(row[0])
        row_count += 1

# die Hash-Werte in einer Liste speicheren
hash_results = []
for key in input_data:
    hash_value = h2(key)
    hash_results.append((key,hash_value))

print(hash_results)


