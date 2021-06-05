import matplotlib as plt
import csv
import pandas as pd
graficos = "Licen-6.xlsx"

df = pd.read_excel(graficos)

print(df.head())

valores = df[["licenciadas", "NO licenciadas"]]
print(valores)
ax = valores.plot.bar(x="licenciadas", y="NO licenciadas", rot = 0)
plt.show()