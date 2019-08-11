#!/usr/bin/env python
# coding: utf-8

########### Módulos ##############
from preprocesamiento import *
from analisis import *
from test_legibilidad import *
from matriz_candidatos import *
########### Fin módulos ##############

diccionario = leer_archivo() #Módulo específico

for i in diccionario:
    print('Cantidad de palabras dichas por',i,': ',len(diccionario[i]),'\n')

#Porcentaje de las palabras totales dichas por cada candidato
labels = [i for i in diccionario]
sizes = [len(diccionario[i]) for i in diccionario]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','red']
#explode = (0, 0, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.title("Porcentaje de las palabras totales dichas por cada candidato")
plt.show()

#ANÁLISIS MACRI
palabras_macri = tokenizacion(diccionario['Macri'])
#Frecuencia de distribución
plot_palabras_mas_usadas(palabras_macri, 'MACRI')
#WordCloud MACRI
plot_wordcloud(palabras_macri, 'MACRI')

#ANÁLISIS STOLBIZER
palabras_stolbizer = tokenizacion(diccionario['Stolbizer'])
#Frecuencia de distribución
plot_palabras_mas_usadas(palabras_stolbizer,'STOLBIZER')
#WordCloud MACRI
plot_wordcloud(palabras_stolbizer,'STOLBIZER')


#ANÁLISIS MASSA
palabras_massa = tokenizacion(diccionario['Massa'])
#Frecuencia de distribución
plot_palabras_mas_usadas(palabras_massa,'MASSA')
#WordCloud MACRI
plot_wordcloud(palabras_stolbizer,'MASSA')


#ANÁLISIS DEL CAÑO
palabras_delcano = tokenizacion(diccionario['Del Caño'])
#Frecuencia de distribución
plot_palabras_mas_usadas(palabras_delcano,'DEL CAÑO')
#WordCloud MACRI
plot_wordcloud(palabras_stolbizer,'DEL CAÑO')


#ANÁLISIS RODRIGUEZ SAÁ
palabras_rodriguezsaa = tokenizacion(diccionario['Rodríguez Saá'])
#Frecuencia de distribución
plot_palabras_mas_usadas(palabras_rodriguezsaa,'RODRÍGUEZ SAÁ')
#WordCloud MACRI
plot_wordcloud(palabras_stolbizer,'RODRÍGUEZ SAÁ')

#TEST LEGIBILIDAD CANDIDATOS
test_legibilidad(diccionario)

#MATRIZ COMPARACIÓN ENTRE CANDIDATOS
#matriz_comparativa('Macri',palabras_macri, 'Stolbizer',palabras_stolbizer)
