#importando las librerias
import pandas as pd
import matplotlib.pyplot as plt


csv = "Big_Japan_vs_China_Technology.csv"
dataframe = pd.read_csv(csv)
year = dataframe["Year"].head() #utilizando head para que aparezcan los primeros cinco datos
star = dataframe["Number of Startups"].head()
print(star)

#creando grafica lineal
x = [166,217,451,264,463]
y = [2001,2011,2009,2019,2002]
plt.plot(x,y,linewidth=3,color="red")
plt.xlabel("startups")
plt.ylabel("Año")
plt.title("China vs Japan")
plt.show()

 #https://www.kaggle.com/datasets/waqi786/china-vs-japan


