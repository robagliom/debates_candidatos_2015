#!/usr/bin/env python
# coding: utf-8

########### Módulos ##############
from preprocesamiento import *
from analisis import *
from test_legibilidad import *
from matriz_candidatos import *
from distancia_coseno import *
from combinaciones import *
from comparacion_macri import *
"""
########### Fin módulos ##############
diccionario = leer_archivo("datos/ArgentinaDebate_2.pdf") #Módulo específico

for i in diccionario:
    print('Cantidad de palabras dichas por',i,': ',len(diccionario[i]),'\n')

#Porcentaje de las palabras totales dichas por cada candidato
labels = [i for i in diccionario]
sizes = [len(diccionario[i]) for i in diccionario]
colors = ['gold','red']
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

#ANÁLISIS SCIOLI
palabras_scioli = tokenizacion(diccionario['Scioli'])
#Frecuencia de distribución
plot_palabras_mas_usadas(palabras_scioli,'SCIOLI')
#WordCloud MACRI
plot_wordcloud(palabras_scioli,'SCIOLI')


#TEST LEGIBILIDAD CANDIDATOS
#COMENTADO HASTA VER ALGO TEÓRICO QUE JUSTIFIQUE
#test_legibilidad(diccionario)

"""
###########################################################
######### ANÁLISIS DISCURSO SEPARADO POR SECCIÓN ##########
print('** Realizamos análisis separado por sección **')
dicc_por_seccion = leer_archivo_separado("datos/ArgentinaDebate_2.pdf")

######### SECCIÓN: DESARROLLO ECONÓMICO Y HUMANO ##########
desarrollo_eco_hum = dicc_por_seccion['Desarrollo económico y humano']['Diccionario']
#preprocesamiento_coseno2(desarrollo_eco_hum,"DESARROLLO ECONÓMICO Y HUMANO: similitud candidatos por distancia del coseno")
#matriz_comparativa(desarrollo_eco_hum,"DESARROLLO ECONÓMICO Y HUMANO: palabras compartidas entre candidatos")

######### SECCIÓN: EDUCACIÓN E INFANCIA ##########
desarrollo_edu_inf = dicc_por_seccion['Educación e infancia']['Diccionario']
#preprocesamiento_coseno2(desarrollo_edu_inf,"EDUCACIÓN E INFANCIA: similitud candidatos por distancia del coseno")
#matriz_comparativa(desarrollo_edu_inf,"EDUCACIÓN E INFANCIA: palabras compartidas entre candidatos")

######### SECCIÓN: SEGURIDAD Y DERECHOS HUMANOS ##########
desarrollo_seg_der = dicc_por_seccion['Seguridad y derechos humanos']['Diccionario']
print(desarrollo_seg_der)
#preprocesamiento_coseno2(desarrollo_seg_der,"SEGURIDAD Y DERECHOS HUMANOS: similitud candidatos por distancia del coseno")
#matriz_comparativa(desarrollo_seg_der,"SEGURIDAD Y DERECHOS HUMANOS: palabras compartidas entre candidatos")

######### SECCIÓN: FORTALECIMIENTO DEMOCRÁTICO ##########
desarrollo_fort_dem = dicc_por_seccion['Fortalecimiento democrático']['Diccionario']
#preprocesamiento_coseno2(desarrollo_fort_dem,"FORTALECIMIENTO DEMOCRÁTICO: similitud candidatos por distancia del coseno")
#matriz_comparativa(desarrollo_fort_dem,"FORTALECIMIENTO DEMOCRÁTICO: palabras compartidas entre candidatos")

comparacion_macri(leer_archivo_separado("datos/Version-taquigrafica.pdf"),dicc_por_seccion,"Relativo")