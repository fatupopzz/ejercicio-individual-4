
#Modulos utilizados
import pandas as pd

#asignacion de los datos
f1 = pd.read_csv('temariof.csv', encoding='ISO-8859-1', delimiter=';')

#Pregunta 1: pista con mas safety cars
p1 = f1['GP'].value_counts().idxmax()

#Top 3 causas mas comunes de safety cars
p2 = f1['Cause'].value_counts().head(3).index.tolist()

#Vuelta con mayor frecuencia en la que se sale el safety car
p3 = f1['Deployed'].value_counts().idxmax()

#cantidad de vueltas “Full Laps” con mayor frecuencia en las que se sale el safety car
p4 = f1['FullLaps'].value_counts().idxmax()

#top 10 de años con mayor cantidad de safety cars
p5 = f1['GP Year'].value_counts().head(10).index.tolist()

#Imprimir los datos
print("La pista con mayor frecuencia de safety cars es: ",p1)
print("Las 3 causas mas comunes de safety cars son: ",p2)
print("La vuelta con mayor frecuencia en la que se sale el safety car es: ",p3)
print("La cantidad de vueltas “Full Laps” con mayor frecuencia en las que se sale el safety car es: ",p4)
print("Los 10 años con mayor cantidad de safety cars son: ",p5)