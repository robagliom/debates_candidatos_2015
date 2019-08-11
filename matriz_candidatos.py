#!/usr/bin/env python
# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

#candidato_i: nombre candidato i (str)
#lista_candidato_i: lista palabras dichas por candidato i (list)
def matriz_comparativa(candidato_1, lista_candidato_1, candidato_2,lista_candidato_2):
    #seteamos listas por si hay elementos repetidos
    lista_candidato_1 = list(set(lista_candidato_1))
    lista_candidato_2 = list(set(lista_candidato_2))
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
    print(lista_candidato_2)
    for i in range(np.shape(matriz)[0]):
        print(lista_candidato_1[i],matriz[i])

    return matriz
