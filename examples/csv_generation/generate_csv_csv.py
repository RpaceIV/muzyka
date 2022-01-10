import testLastfm.py as fm
import csv

# Create a list of column names.
columns = ['song', 'artist', 'genre', 'subgenre', 'q1', 'q2', 'q3', 'q4', 'q5']

# Create a list of rows that match the column's data.
rows = [
    ['Martini Blue', 'DPR Live', 'Rap', 'K-Pop',
        'a', 'a', 'b', 'c', 'a']
]

# Create a filename.
filename = "testMuzyka.csv"

# Open filename that writes in the columns and rows variables.
with open(filename, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(columns)
    writer.writerows(rows)
