#!/usr/bin/env python
# coding: utf-8

########### Módulos ##############
from preprocesamiento import *
from analisis import *
from test_legibilidad import *
from matriz_candidatos import *
from distancia_coseno import *
from combinaciones import *
########### Fin módulos ##############
"""
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
#COMENTADO HASTA VER ALGO TEÓRICO QUE JUSTIFIQUE
#test_legibilidad(diccionario)
"""


###########################################################
######### ANÁLISIS DISCURSO SEPARADO POR SECCIÓN ##########
print('** Realizamos análisis separado por sección **')
dicc_por_seccion = leer_archivo_separado()

######### SECCIÓN: DESARROLLO ECONÓMICO Y HUMANO ##########
print('Sección: DESARROLLO ECONÓMICO Y HUMANO')
desarrollo_eco_hum = dicc_por_seccion['Desarrollo económico y humano']['Diccionario']

palabras_macri = desarrollo_eco_hum['Macri']
palabras_stolbizer = desarrollo_eco_hum['Stolbizer']
palabras_massa = desarrollo_eco_hum['Massa']
palabras_delcano = desarrollo_eco_hum['Del Caño']
palabras_rodriguezsaa = desarrollo_eco_hum['Rodríguez Saá']

dic_desarrollo_eco_hum = {
                        'Macri':palabras_macri,
                        'Stolbizer':palabras_stolbizer,
                        'Massa':palabras_massa,
                        'Del Caño':palabras_delcano,
                        'Rodríguez Saá':palabras_rodriguezsaa,
                        }

#DISTANCIA DEL COSENO
print('Calculamos distancia del coseno para cada par de candidatos')
"""combinaciones = combinaciones(list(dic_desarrollo_eco_hum.keys()),2)
lista_cosenos =[] #0:candidato 1 || 1: candidato 2 || 2: valor coseno
for c in combinaciones:
    print(c)
    cosine = get_cosine(dic_desarrollo_eco_hum[c[0]],dic_desarrollo_eco_hum[c[1]])
    print('Coseno entre {} y {}:'.format(c[0],c[1]), cosine)
    lista_cosenos.append([c[0],c[1],cosine])"""

lista_cosenos = [] #Macri | Stolbizer | Massa | Del Caño | Rodríguez Saá
for c1 in dic_desarrollo_eco_hum:
    lista_aux_cos = []
    for c2 in dic_desarrollo_eco_hum:
        coseno = get_cosine(dic_desarrollo_eco_hum[c1],dic_desarrollo_eco_hum[c2])
        lista_aux_cos.append(coseno)
    lista_cosenos.append(lista_aux_cos)

fila =list(dic_desarrollo_eco_hum.keys())
columna = fila
tabla_coseno(fila,columna,lista_cosenos,"DESARROLLO ECONÓMICO Y HUMANO: compartación candidatos por método del coseno")

#MATRIZ COMPARACIÓN ENTRE CANDIDATOS
#matriz_comparativa('Macri',desarrollo_eco_hum['Macri'], 'Stolbizer',desarrollo_eco_hum['Stolbizer'])
