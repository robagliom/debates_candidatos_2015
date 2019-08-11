#!/usr/bin/env python
# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

from analisis import *

def tabla_palabras_comun(fila,columna,lista,titulo):
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

def intersect(a, b):
    return list(set(a) & set(b))

def matriz_comparativa(seccion,titulo):
    palabras_macri = tokenizacion(seccion['Macri'])
    palabras_stolbizer = tokenizacion(seccion['Stolbizer'])
    palabras_massa = tokenizacion(seccion['Massa'])
    palabras_delcano = tokenizacion(seccion['Del Caño'])
    palabras_rodriguezsaa = tokenizacion(seccion['Rodríguez Saá'])

    dic_seccion = {
                'Macri':palabras_macri,
                'Stolbizer':palabras_stolbizer,
                'Massa':palabras_massa,
                'Del Caño':palabras_delcano,
                'Rodríguez Saá':palabras_rodriguezsaa,
                }

    lista_comun = [] #Macri | Stolbizer | Massa | Del Caño | Rodríguez Saá
    for c1 in dic_seccion:
        lista_aux_comun = []
        for c2 in dic_seccion:
            interseccion = intersect(dic_seccion[c1],dic_seccion[c2])
            lista_aux_comun.append(len(interseccion))
        lista_comun.append(lista_aux_comun)

    fila =list(dic_seccion.keys())
    columna = fila
    tabla_palabras_comun(fila,columna,lista_comun,titulo)

"""    #print('1',candidato_1,lista_candidato_1)
    #seteamos listas por si hay elementos repetidos
    lista_candidato_1 = tokenizacion(lista_candidato_1)#list(set(lista_candidato_1))
    lista_candidato_2 = tokenizacion(lista_candidato_2)#list(set(lista_candidato_2))
    #print('2',candidato_1,lista_candidato_1)
    #creamos matriz de orden cantidad de palabras del candidato 1 por las del candidato 2
    matriz = np.empty((len(lista_candidato_1), len(lista_candidato_2)))
    #print(np.shape(matriz)[0],np.shape(matriz)[1])
    for i in range(np.shape(matriz)[0]):
        for j in range(np.shape(matriz)[1]):
            #print(lista_candidato_1[i],lista_candidato_2[j])
            if lista_candidato_1[i] == lista_candidato_2[j]:
                matriz[i][j] = 1
                #print('SIIIIIIIIIIIII************************')
    #print(matriz)
    #tendría que crear un excel
    print("{} vs {}".format(candidato_1,candidato_2))
    #print(lista_candidato_2)
    #for i in range(np.shape(matriz)[0]):
    #    print(lista_candidato_1[i],matriz[i])

    return matriz"""
