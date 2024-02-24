import matplotlib.pyplot as plt #importo las librerías necesarias para trabajar
import numpy as np


y1 = [36.3 , 36.5 , 36.7 , 37.2 , 36.9 , 36.6]  #creo tres listas con los valores de temperatura de cada día
y2 = [36.2 , 36.4 , 36.7 , 37 , 36.6 , 36.6]
y3 = [36.3 , 36.6 , 36.7 , 36.9 , 36.7 , 36.6]

y = y1+y2+y3 #fusiono las listas en una sola


x = ['9:00' , '12:00' , '15:00' , '18:00' , '21:00' , '00:00']*3 #creo una lista con las horas (la amplío hasta el triple con los mismos valores)


x_values = list(np.arange(len(x))) #creo un array de valores según la cantidad de valores de la lista anterior y lo transformo en una lista 

plt.plot(x_values, y, marker='o', color = "c", markersize=4) #creo un plot (gráfico de líneas) con los valores de las lista x_values según la hora (valores de la lista y)

plt.xticks(x_values, x, fontsize=5) #a cada valor dado anteriormente en el array (x_values) le asigno como etiqueta cada valor de la lista x y los coloco en el eje x


#aquí estoy creando una lista para los valores del eje y

lista = []

z=36.0
lista.append(z)

for i in range(15):
  x=0.1
  z+=x
  i+1
  lista.append(round(z, 1))

#---------------------------

plt.yticks(lista, fontsize=7) #coloco los valores de la lista en el eje y

plt.xlabel("Tiempo (horas)", labelpad=7)  #asigno las etiquetas de cada eje
plt.ylabel("Temperatura (ºC)")

plt.savefig('filename.png', dpi=300) #guardo el archivo para añadirlo al documento word