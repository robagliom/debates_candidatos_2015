from classifier import *
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import yticks, xticks
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import numpy as np
from preprocesamiento import leer_archivo_separado

def sentimiento_oraciones(dicc_por_seccion):
    #Una vez separadas las oraciones en dicc_por_seccion, analizamos y graficamos la positividad/negatividad de cada una
    #dicc_por_seccion["Desarrollo económico y humano"]["Diccionario"]["Macri"]
    clf = SentimentClassifier()
    datos = {}
    del dicc_por_seccion["Introducción"]
    #Para cada sección
    for key in list(dicc_por_seccion.keys()):
        datos[key] = {}
        #Para cada candidato
        for candidato in list(dicc_por_seccion[key]["Oraciones"].keys()):
            oraciones = dicc_por_seccion[key]["Oraciones"][candidato]
            sentimientos = [clf.predict(i) for i in oraciones]
            datos[key][candidato] = sentimientos
    
    cats = list(dicc_por_seccion.keys())
    candidatos = list(dicc_por_seccion[key]["Oraciones"].keys())
    for cat in cats:
        colores = ["#003f5c","#58508d","#bc5090","#ff6361","#ffa600"]
        datos_totales = []
        largos = [0]
        for candidato in candidatos:
            print(candidato)
            datos_totales += datos[cat][candidato]
            largos.append(len(datos[cat][candidato]) + largos[-1])      
            plt.hlines(y=np.mean(datos[cat][candidato]), xmin=largos[-2], xmax=largos[-1], linewidth=1, color='black')
        print(largos)  
        barlist = plt.bar(range(len(datos_totales)),datos_totales)
        for l in range(1,len(largos)):
            c = colores.pop()
            for i in range(largos[l-1],largos[l]):
                barlist[i].set_color(c)
        plt.title(str("Sentimientos en categoría "+cat))
        legend_elements = [Patch(facecolor='#ffa600', edgecolor='#ffa600',
                           label=candidatos[0]),
                           Patch(facecolor='#ff6361', edgecolor='#ff6361',
                           label=candidatos[1]),
                           Patch(facecolor='#bc5090', edgecolor='#bc5090',
                           label=candidatos[2]),
                           Patch(facecolor='#58508d', edgecolor='#58508d',
                           label=candidatos[3]),
                           Patch(facecolor='#003f5c', edgecolor='#003f5c',
                           label=candidatos[4]),
                           Line2D([0], [0], color='black', lw=4,label='Promedio')]
        xticks([i+((len(datos_totales))/10) for i in largos[:-1]], candidatos)
        plt.legend(handles=legend_elements)
        yticks([0,0.5,1], ('Más negativo','Neutro', 'Más Positivo'))
        plt.show()
