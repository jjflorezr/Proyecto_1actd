import matplotlib.pyplot as plt

# Datos
nombres = ['A', 'B', 'C', 'D']
valores = [10, 20, 30, 40]

# Crear el diagrama de barras
plt.bar(nombres, valores)

# Personalizar el gráfico
plt.title('Mi diagrama de barras')
plt.xlabel('Nombres')
plt.ylabel('Valores')

# Mostrar el gráfico
plt.show()