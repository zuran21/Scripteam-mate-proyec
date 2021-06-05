import matplotlib.pyplot as plt
import numpy as np


np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()


Universidades = ('Licenciadas', 'No licenciadas')
y_pos = np.arange(len(Universidades))
Cantidad1 = (15, 30)
cantidad2 = (30, 15)


ax.barh(y_pos, Cantidad1, cantidad2, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(Universidades)
ax.invert_yaxis() 
ax.set_xlabel('Performance')
ax.set_title('Licensamiento de Universidades')

plt.show()