#!/usr/bin/env python
# coding: utf-8

########### Módulos ##############
from preprocesamiento import *
from analisis import *
from legibilidad import *
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
results = {"Macri":{},"Stolbizer":{},"Massa":{},"Del Caño":{},"Rodríguez Saá":{}}

for key in list(results.keys()):
    results[key]["INFLESZ"] = fernandez_huerta(diccionario[key])
    results[key]["Szigriszt Pazos"] = szigriszt_pazos(diccionario[key])
    results[key]["Gutierrez"] = gutierrez(diccionario[key])
    results[key]["Mu"] = mu(diccionario[key])
    results[key]["Crawford"] = crawford(diccionario[key])

rows = [key for key in list(results.keys())]
columns = [key for key in list(results[rows[0]].keys())]
data = [[0 for i in range(len(columns))] for j in range(len(rows))]

for r in range(len(rows)):
    for c in range(len(columns)):
        data[r][c] = results[rows[r]][columns[c]]

fig=plt.figure()
ax = plt.gca()
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
tbl = ax.table(cellText=data,rowLabels=rows,colLabels=columns,loc='center',colWidths=[0.08 for x in columns])
tbl.scale(0.6*2,1.5*2)
plt.title("Comparación de complejidad de textos de todos los candidatos por múltiples métodos")
plt.show()



data = []
columns = []
for key in list(results.keys()):
    columns.append(key + "\n"+ str(results[key]["INFLESZ"]))
    data.append(results[key]["INFLESZ"])

plt.figure()
plt.bar(columns,data)
plt.title("Análisis de complejidad de texto por método INFLESZ")
plt.ylim(60,70)
plt.show()
