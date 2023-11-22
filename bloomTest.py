import csv
import matplotlib.pyplot as plt
from hash1 import h1
from hash2 import h2

from bloom import BloomFilter
# Erwartete Anzahl von Elementen


# Filter Größe als Bits, um die false positive Rate von 0.05 zu erreichen
filter_size = 79022

# Erstellen eines Bloom-Filters
hash_functions = [h1, h2] 
bloom = BloomFilter(filter_size, hash_functions)

# import Elemente
test_elements = []
with open('da_DK.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        test_elements.extend(row)

#  Auswahl von 10.000 Testelementen aus der Liste
anzahl_test_elementen = 10000
selected_test_elements = test_elements[:anzahl_test_elementen]

# Einfügen der ausgewählten Testelemente in den Bloom-Filter

for element in selected_test_elements:
    bloom.insert(element)


false_positives = 0

# Auswahl von 10.000 Testelementen, die nicht im Filter enthalten sind
test_elements_not_in_filter = test_elements[10000:]


for element in test_elements_not_in_filter:
    if bloom.search(element):
        false_positives += 1
        
    
false_positive_ratio = false_positives / len(test_elements)
#print(len(test_elements_not_in_filter))
# Ausgabe der Ergebnisse
print(f"Optimale Filtergröße: {filter_size} Bits")
print(f"Fehlerwahrscheinlichkeit: {false_positive_ratio}")
print(f"falsch positiven Ergebnisse: {false_positives} von {len(test_elements)}")