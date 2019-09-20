#!/usr/bin/env python
# coding: utf-8

#Vamos a procesar los datos del discurso para ver cómo se nombra al oficialismo
from preprocesamiento import *
from analisis import *

primer_debate = leer_archivo("datos/Version-taquigrafica.pdf")
segundo_debate = leer_archivo("datos/ArgentinaDebate_2.pdf")

#print(primer_debate)

def buscar_palabras(primer_debate):
    with open('oficialismo/nombres_oficialismo.txt', 'r') as f:
        palabras_oficialismo = [linea.replace('\n','') for linea in f]

    oficialismo = {}
    for candidato in primer_debate.keys():
        lista = []
        #print(candidato)
        palabras = tokenizacion(primer_debate[candidato])
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
def buscar_oraciones(primer_debate):
    dic_oraciones = {}
    oficialismo = buscar_palabras(primer_debate)
    for candidato in primer_debate.keys():
        lista_candidato = []
        oraciones = primer_debate[candidato].split('.')
        palabras_candidato = set(oficialismo[candidato])
        for oracion in oraciones:
            for palabra in palabras_candidato:
                if palabra in oracion:
                    lista_candidato.append(oracion)

        dic_oraciones[candidato] = lista_candidato
    print(dic_oraciones)
    return dic_oraciones,oficialismo

#primer debate octubre 2015
oraciones_primer_debate=buscar_oraciones(primer_debate)
oraciones_segundo_debate=buscar_oraciones(segundo_debate)

print('PRIMER DEBATE',oraciones_primer_debate)
print('SEGUNDO DEBATE',oraciones_segundo_debate)
