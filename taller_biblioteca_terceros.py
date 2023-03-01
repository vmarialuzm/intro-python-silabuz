import pandas as pd

df = pd.read_csv("titanic.csv")

suma_edades = df["Age"].sum()
total_mujeres = df["Sex"][df["Sex"]=="female"].count()
total_hombres = df["Sex"][df["Sex"]=="male"].count()
total_sobrevivientes = df["Survived"][df["Survived"]==1].count()
total_fallecidos = df["Survived"][df["Survived"]==0].count()

print(f"Promedio edad: {suma_edades/len(df):.2f}")
print("Total hombres:", total_hombres)
print("Total mujeres:", total_mujeres)
print("Total sobrevivientes:", total_sobrevivientes)
print("Total fallecidos:", total_fallecidos)



import requests

response = requests.get("http://www.google.com/")
print(response)



import json

f=open('personas.json')

data = json.load(f)
print(data)



