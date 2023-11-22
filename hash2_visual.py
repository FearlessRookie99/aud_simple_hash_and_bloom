import csv
import matplotlib.pyplot as plt
from hash2 import h2


input_file  = 'da_DK.csv'
hashed_rows = 100000

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

#Liste nur mit hash Ausgaben, um dies visualisieren zu können 
hash_values_visual = [item[1] for item in hash_results]
#Visualisiere die Verteilung der Hash-Werte in einem Histogramm
plt.hist(hash_values_visual, bins=2000, alpha=0.5, color='b', edgecolor='black')
plt.xlabel('Hash-Wert')
plt.ylabel('Anzahl')
plt.title('Verteilung der Hash-Werte')
plt.grid(True)
plt.show()