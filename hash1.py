import csv
import matplotlib.pyplot as plt


input_file  = 'da_DK.csv'
hashed_rows = 100000
def h1(key, hash_size=100003):
    # Verwende den Anfangsbuchstaben
    key_value = ord(key[0])
    square = key_value ** 2
    hash_str = str(square)
    
    # Fülle den String mit Nullen auf, um die gewünschte STRING länge zu erreichen
    while len(hash_str) < 7:
        hash_str = '0' + hash_str
        
    # Verwende die mittleren Stellen als Hash-Wert
    start = (len(hash_str) // 3)
    end = start + (len(str(hash_size))//2)
    hash_value = int(hash_str[start:end]) 
    hash_value = hash_value ** 2
    
    
    # Iteriere über die restlichen Zeichen des Schlüssels 
    # durch % hash-size, um die Werte zu mischen 
    for char in key[1:]:
        hash_value = (hash_value * 256 + ord(char)) % hash_size
        
    
    
   
    # verwende die letze Buchstabe als multiplikationsfaktor
    key_value2 = ord(key[len(key)-1]) 
    key_value2= key_value2 ** 2
    hash_value = hash_value * key_value2
    
     #verwenden von konstanten 
    if hash_value >= 20000 : 
        hash_value = hash_value * 2.3289462
    elif hash_value >= 40000 : 
        hash_value = hash_value * 0.5595924
    elif hash_value >= 60000 : 
        hash_value = hash_value * 3.5989295
    elif hash_value >= 80000 : 
        hash_value = hash_value * 0.78942956
    else: 
        hash_value = hash_value * 1.2323323
   
    #gesammte hash_value auf hash_size verteilen 
    hash_value = hash_value % hash_size
    
    #Ergebnis auf Ganze Zahlen aufrunden 
    hash_value=int(hash_value)
    return hash_value

# Eingabe aus einer CSV-Datei lesen und in einer Liste speichern 

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
    hash_value = h1(key)
    hash_results.append((key,hash_value))

print(hash_results)