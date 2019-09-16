#!/usr/bin/env python
# coding: utf-8
import re, math
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
    vec1 = text_to_vector(vec1)
    vec2 = text_to_vector(vec2)

    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        #similitud 1-distancia
        return abs(round(1 - float(numerator) / denominator,4))

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

def tabla_coseno(fila,columna,lista,titulo):
    fig = plt.figure()
    ax = plt.gca()
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    col_labels = columna
    row_labels = fila
    table_vals = lista#[[11, 12, 13,0,0], [21, 22, 23,0,0], [31, 32, 33,0,0], [31, 32, 33,0,0], [31, 32, 33,0,0]]

    # Draw table
    the_table = ax.table(cellText=table_vals,
                          colWidths=[0.05] * 5,
                          rowLabels=row_labels,
                          colLabels=col_labels,
                          loc='center')
    the_table.scale(0.5*5,1.5*4)
    plt.title(titulo)
    plt.show()

def preprocesamiento_coseno(seccion,titulo):
    palabras_macri = seccion['Macri']
    palabras_stolbizer = seccion['Stolbizer']
    palabras_massa = seccion['Massa']
    palabras_delcano = seccion['Del Caño']
    palabras_rodriguezsaa = seccion['Rodríguez Saá']

    dic_seccion = {
                            'Macri':palabras_macri,
                            'Stolbizer':palabras_stolbizer,
                            'Massa':palabras_massa,
                            'Del Caño':palabras_delcano,
                            'Rodríguez Saá':palabras_rodriguezsaa,
                            }

    #DISTANCIA DEL COSENO
    """combinaciones = combinaciones(list(dic_desarrollo_eco_hum.keys()),2)
    lista_cosenos =[] #0:candidato 1 || 1: candidato 2 || 2: valor coseno
    for c in combinaciones:
        print(c)
        cosine = get_cosine(dic_desarrollo_eco_hum[c[0]],dic_desarrollo_eco_hum[c[1]])
        print('Coseno entre {} y {}:'.format(c[0],c[1]), cosine)
        lista_cosenos.append([c[0],c[1],cosine])"""

    lista_cosenos = [] #Macri | Stolbizer | Massa | Del Caño | Rodríguez Saá
    for c1 in dic_seccion:
        lista_aux_cos = []
        for c2 in dic_seccion:
            coseno = get_cosine(dic_seccion[c1],dic_seccion[c2])
            lista_aux_cos.append(coseno)
        lista_cosenos.append(lista_aux_cos)

    fila =list(dic_seccion.keys())
    columna = fila
    tabla_coseno(fila,columna,lista_cosenos,titulo)


def preprocesamiento_coseno2(seccion,titulo):
    palabras_macri = seccion['Macri']
    palabras_scioli = seccion['Scioli']

    dic_seccion = {
                            'Macri':palabras_macri,
                            'Scioli':palabras_scioli,
                            }

    #DISTANCIA DEL COSENO
    """combinaciones = combinaciones(list(dic_desarrollo_eco_hum.keys()),2)
    lista_cosenos =[] #0:candidato 1 || 1: candidato 2 || 2: valor coseno
    for c in combinaciones:
        print(c)
        cosine = get_cosine(dic_desarrollo_eco_hum[c[0]],dic_desarrollo_eco_hum[c[1]])
        print('Coseno entre {} y {}:'.format(c[0],c[1]), cosine)
        lista_cosenos.append([c[0],c[1],cosine])"""

    lista_cosenos = [] #Macri | Stolbizer | Massa | Del Caño | Rodríguez Saá
    for c1 in dic_seccion:
        lista_aux_cos = []
        for c2 in dic_seccion:
            coseno = get_cosine(dic_seccion[c1],dic_seccion[c2])
            lista_aux_cos.append(coseno)
        lista_cosenos.append(lista_aux_cos)

    fila =list(dic_seccion.keys())
    columna = fila
    tabla_coseno(fila,columna,lista_cosenos,titulo)
