import sys
import json 

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem
)

json_file = sys.argv[1]

try:
    with open(json_file, encoding="utf-8") as f:
        data = json.load(f)
        print(type(data))
except:
    print(f"Can't load the data from {json_file}")

app = QApplication([])
table = QTableWidget()
table.setRowCount(len(data))
table.setColumnCount(len(data[0]))
table.setHorizontalHeaderLabels(data[0].keys())
#for loop row and column

num_rows = len(data)
num_cols = len(data[0])

table.setSortingEnabled(True)

#passing through all the indexes in a table startinng from 0,0, adding the value by converting
for col in range(num_cols):
    for row in range(num_rows):
        valeur_courrante = str(list(data[row].values())[col])#it takes the data of the current row, takes only the data, transforms it into a list(because lists stores also the index) and then makes sure that all of this is a str
        table.setItem(row, col, QTableWidgetItem(valeur_courrante) )
   
window = QMainWindow()
window.setCentralWidget(table)
window.show()
sys.exit(app.exec())








    




