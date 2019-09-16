#!/usr/bin/env python
# coding: utf-8

from preprocesamiento import *

# NLTK: kit de herramientas de lenguaje natural
import nltk #https://www.nltk.org/

import operator

import numpy as np

import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

from wordcloud import WordCloud

def tokenizacion(lista):
    #Tokenización
    #divide cadenas de texto más largas en piezas más pequeñas o tokens
    palabras = nltk.word_tokenize(lista)

    palabras = normalize(palabras)

    #Quitamos palabras ruido
    palabras_filtradas=[]
    for w in palabras:
        if w not in stop_words:
            palabras_filtradas.append(w)
    return palabras_filtradas

#devuelve histograma con las 50 frecuencias mas altas
#recibe lista y dato para xlabel
def plot_palabras_mas_usadas(lista,titulo):
    #Frecuencia de distribución
    fdist = FreqDist(lista)

    resultado = sorted(fdist.items(), key=operator.itemgetter(1))
    resultado.reverse()
    #print(resultado[:50])

    x = np.arange(50)
    plt.title(str(titulo))
    plt.bar(x, [i[1] for i in resultado[:50]])
    plt.xticks(x, (i[0] for i in resultado[:50]),rotation='vertical')
    plt.show()
    #mas_usadas = [i[0] for i in resultado[:50]]
    #return mas_usadas#plt

#WordCloud
#recibe lista y dato para xlabel
def plot_wordcloud(lista,titulo):
    wc = WordCloud(width=1000,height=1000,background_color="White",max_words=150).generate(' '.join((lista)))
    plt.figure()
    plt.title(str(titulo))
    plt.imshow(wc,interpolation='bilinear')
    plt.axis("off")
    plt.show()
