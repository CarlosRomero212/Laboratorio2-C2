# Importando las librerías
import pandas as pd
import matplotlib.pyplot as plt


csv = "gym_members_exercise_tracking.csv"
dataframe = pd.read_csv(csv)


Age = dataframe["Age"].value_counts().head()  
print(Age)


op = Age.index.astype(str)  
fre = Age.values  

# Definir colores para las barras
colores = ["pink", "blue", "brown", "purple", "orange"]

# Crear el gráfico de barras
plt.figure(figsize=(10, 6)) 
plt.bar(op, fre, color=colores[:len(op)], linewidth=3)  
plt.title("viajes al espacio")
plt.xlabel("viajes")
plt.ylabel("Cantidad de Miembros")
plt.xticks(rotation=45)  
plt.tight_layout()
plt.show()



#https://www.kaggle.com/datasets/pinuto/nasa-close-approach-data-2023-2024
#En el siguiente grafico se puede visualizar las edades de las personas que asisten al gym 
# y la cantidad de personas que tienen esa edad.