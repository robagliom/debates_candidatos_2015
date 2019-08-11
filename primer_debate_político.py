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


###########################################################
######### ANÁLISIS DISCURSO SEPARADO POR SECCIÓN ##########
print('** Realizamos análisis separado por sección **')
dicc_por_seccion = leer_archivo_separado()

######### SECCIÓN: DESARROLLO ECONÓMICO Y HUMANO ##########
desarrollo_eco_hum = dicc_por_seccion['Desarrollo económico y humano']['Diccionario']
preprocesamiento_coseno(desarrollo_eco_hum,"DESARROLLO ECONÓMICO Y HUMANO: similitud candidatos por distancia del coseno")
matriz_comparativa(desarrollo_eco_hum,"DESARROLLO ECONÓMICO Y HUMANO: palabras compartidas entre candidatos")

######### SECCIÓN: EDUCACIÓN E INFANCIA ##########
desarrollo_edu_inf = dicc_por_seccion['Educación e infancia']['Diccionario']
preprocesamiento_coseno(desarrollo_edu_inf,"EDUCACIÓN E INFANCIA: similitud candidatos por distancia del coseno")
matriz_comparativa(desarrollo_edu_inf,"EDUCACIÓN E INFANCIA: palabras compartidas entre candidatos")

######### SECCIÓN: SEGURIDAD Y DERECHOS HUMANOS ##########
desarrollo_seg_der = dicc_por_seccion['Seguridad y derechos humanos']['Diccionario']
preprocesamiento_coseno(desarrollo_seg_der,"SEGURIDAD Y DERECHOS HUMANOS: similitud candidatos por distancia del coseno")
matriz_comparativa(desarrollo_seg_der,"SEGURIDAD Y DERECHOS HUMANOS: palabras compartidas entre candidatos")

######### SECCIÓN: FORTALECIMIENTO DEMOCRÁTICO ##########
desarrollo_fort_dem = dicc_por_seccion['Fortalecimiento democrático']['Diccionario']
preprocesamiento_coseno(desarrollo_fort_dem,"FORTALECIMIENTO DEMOCRÁTICO: similitud candidatos por distancia del coseno")
matriz_comparativa(desarrollo_fort_dem,"FORTALECIMIENTO DEMOCRÁTICO: palabras compartidas entre candidatos")
