# Importando las librerías
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
csv = "gym_members_exercise_tracking.csv"
dataframe = pd.read_csv(csv)

# Obtener las 5 edades más comunes
Age = dataframe["Age"].value_counts().head()  # Utilizando head para que aparezcan los primeros cinco datos
print(Age)

# Crear gráfico circular con los datos del dataset de gym
# Usar los índices y valores de Age directamente
op = Age.index.astype(str)  # Convertir índices a string para las etiquetas
fre = Age.values  # Usar los valores directamente

# Crear el gráfico circular
plt.figure(figsize=(8, 8))  # Ajustar el tamaño de la figura
plt.pie(fre, labels=op, autopct='%1.1f%%', startangle=90, colors=["pink", "blue", "brown", "purple", "orange"])
plt.title("Distribución de Edades de los Miembros del Gimnasio")
plt.axis('equal')  # Para que el gráfico sea un círculo
plt.tight_layout()  # Ajustar el diseño para evitar superposiciones
plt.show()

#https://www.kaggle.com/datasets/valakhorasani/gym-members-exercise-dataset
# En el siguiente gráfico se puede visualizar la proporción de edades de las personas que asisten al gimnasio 
# en relación con el total de miembros, permitiendo una fácil comparación entre las diferentes edades.
