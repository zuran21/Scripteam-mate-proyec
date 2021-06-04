import matplotlib as plt
import numpy as np
import csv

with open('csv/Licenciamiento_Institucional_6.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter="|")
    for row in reader:
        print("CODIGO: {0}, NOMBRE: {1}, TIPO_GESTION: {2}, ESTADO_LICENCIAMIENTO: {3}".format(row[0], row[1], row[2], row[3]))