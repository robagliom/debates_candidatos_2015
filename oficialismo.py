#!/usr/bin/env python
# coding: utf-8

#Vamos a procesar los datos del discurso para ver cómo se nombra al oficialismo
from preprocesamiento import *
from analisis import *

archivo = leer_archivo()
#print(archivo)

def buscar_palabras(archivo):
    with open('oficialismo/nombres_oficialismo.txt', 'r') as f:
        palabras_oficialismo = [linea.replace('\n','') for linea in f]

    oficialismo = {}
    for candidato in archivo.keys():
        lista = []
        #print(candidato)
        palabras = tokenizacion(archivo[candidato])
        #print(palabras)
        for word in palabras:
            #print(word)
            if word in palabras_oficialismo:
                lista.append(word)
        oficialismo[candidato] = lista

    print('palabras_oficialismo',oficialismo)
    #diccionario oficialismo: {candidato:[palabras dichas]}
    return oficialismo

#Recibe diccionario con lo que dijo cada candidato
def buscar_oraciones(archivo):
    dic_oraciones = {}
    oficialismo = buscar_palabras(archivo)
    for candidato in archivo.keys():
        lista_candidato = []
        oraciones = archivo[candidato].split('.')
        palabras_candidato = set(oficialismo[candidato])
        for oracion in oraciones:
            for palabra in palabras_candidato:
                if palabra in oracion:
                    lista_candidato.append(oracion)

        dic_oraciones[candidato] = lista_candidato
    print(dic_oraciones)
    return dic_oraciones

#primer debate octubre 2015
buscar_oraciones(archivo)
