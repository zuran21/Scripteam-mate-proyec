import matplotlib as plt
import numpy as np
import csv

with open('licenciamiento.csv', encoding='uft-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print("CODIGO_ENTIDAD: {0}, NOMBRE: {1}, TIPO_GESTION: {2}, ESTADO_LICENCIAMIENTO: {3}".format(row[0], row[1], row[2], row[3]))