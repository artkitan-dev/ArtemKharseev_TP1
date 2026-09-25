import sys
import json 

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QLineEdit,
    QWidget,
    QAbstractItemView,
    QLabel, 
    QHBoxLayout
)

from PySide6.QtCore import Qt

#reading json
def load_data(json_file):#loads the jason file
    try:
        with open(json_file) as f:
            data = json.load(f)
            print(type(data))
    except:
        #exit with a message if anything goes wrong
        print(f"Can't load the data from {json_file}")
        sys.exit(1)
    return data
#creating visual table(empty without data)
def create_table(data):
    app = QApplication([])
    table = QTableWidget()
    table.setRowCount(len(data))# row per dictionary
    table.setColumnCount(len(data[0]))# one column per key
    table.setHorizontalHeaderLabels(data[0].keys())#keys are the titles 
    #sort by click
    table.setSortingEnabled(True)
    #blocks the user from writing in the table
    table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    return table,app
#putting data in the table
def fill_table(table, data):
    num_rows = len(data)#counts dictionnaires
    num_cols = len(data[0])#counts items
    #passing through all the indexes in a table startinng from 0,0, adding the value by converting - loop
    for col in range(num_cols):
        for row in range(num_rows):
            #it takes the data of the current row, takes only the values, transforms it into a list(because lists stores also the index) and then makes sure that all of this is a str
            valeur_courrante = str(list(data[row].values())[col])
            table.setItem(row, col, QTableWidgetItem(valeur_courrante))
    #print(data[0]["prix"])

def create_window(table, search_input, info):#assembles everything
    window = QMainWindow()

    layout = QVBoxLayout()
    layout.addLayout(info)
    layout.addWidget(search_input)
    layout.addWidget(table)

    container = QWidget()
    container.setLayout(layout)

    window.setCentralWidget(container)
    return window
#reaction to search
def search(table, typed):
        #clear current selection
        table.setCurrentItem(None)

        if not typed:
            # Empty string, don't search
            return

        matching_items = table.findItems(typed, Qt.MatchContains)
        if matching_items:
            # we have found something
            item = matching_items[0]  # take the first
            table.setCurrentItem(item)
#front-end search
def create_search(table):
    search_input = QLineEdit()#search bar
    search_input.setPlaceholderText("Search")
    search_input.textChanged.connect(lambda typed: search(table, typed))
    return search_input

def calc_taille_fichier(data, key):
    total = 0
    for line in data:
        total += float(line[key].replace(" MB", ""))#convertir en chiffre(float)
    return total

def create_info(nom, size, dics):
    info = QHBoxLayout()#arranges horizontally
    info_nom = QLabel(f"Fichier: {nom}")
    info_taille = QLabel(f"Taille du tableau: {size} MB")
    info_elements = QLabel(f"Nombre d'éléments: {dics}")

    info.addWidget(info_nom)
    info.addWidget(info_taille)
    info.addWidget(info_elements)

    return info
    

def main():
    data = load_data(sys.argv[1])
    table,app = create_table(data)
    fill_table(table, data)
    search_input = create_search(table)

    nom = "TP1 - Artem Kharseev"
    taille = calc_taille_fichier(data, "taille_fichier")
    elements = len(data)
    info = create_info(nom, taille, elements)

    window = create_window(table, search_input,info)
    window.show()
    sys.exit(app.exec())   

w = main()
w.show()
