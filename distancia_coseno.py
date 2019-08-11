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
        return round(float(numerator) / denominator,4)

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

    # Removing ticks and spines enables you to get the figure only with table
    """plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=False)
    for pos in ['right','top','bottom','left']:
        plt.gca().spines[pos].set_visible(False)
    plt.savefig('tabla_cosenos.png', bbox_inches='tight', pad_inches=0.05)"""
