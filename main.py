#from src.utils.loader import get_table_from_url
import matplotlib.pyplot as plt
import src.utils.loader as loader

url1 = 'https://clasico.rava.com/empresas/precioshistoricos.php?e=GD30D'
df1 = loader.get_table_from_url(url1, 'GD30D')

#print(df1.tail())


# Crear un gráfico
plt.figure(figsize=(10, 5))
plt.plot(df1['Fecha'], df1['Cierre_GD30D'], label='Precio GD30D')
plt.xlabel('Fecha')
plt.ylabel('Cierre_GD30D')
plt.title('Precio Histórico de GD30D')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()