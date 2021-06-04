import matplotlib.pyplot as plt
from matplotlib.style.core import read_style_directory

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
Estado = 'Licenciadas', 'No licenciadas'
sizes = [15, 30]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=Estado, autopct='%1.1f%%')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()