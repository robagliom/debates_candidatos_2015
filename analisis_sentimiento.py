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
    #dicc_por_seccion["Desarrollo económico y humano"]["Oraciones"]["Macri"]

    #Instanciamos el analizador de sentimientos
    clf = SentimentClassifier()

    #Creamos un diccionario tal que: Datos[Desarrollo económico y humano"]["Macri"] = [0.22,0.11,0.98...]
    datos = {}

    #Borramos la introduccion
    del dicc_por_seccion["Introducción"]

    #Para cada sección:
    for key in list(dicc_por_seccion.keys()):
        datos[key] = {}
        #Para cada candidato
        for candidato in list(dicc_por_seccion[key]["Oraciones"].keys()):
            #Obtenemos las oraciones de ese candidato
            oraciones = dicc_por_seccion[key]["Oraciones"][candidato]
            #Creamos un arreglo de positividad de esas oraciones
            sentimientos = [clf.predict(i) for i in oraciones]
            #Lo guardamos en datos
            datos[key][candidato] = sentimientos

    grafico_barras(datos)
    #grafico_lineas(datos)


def grafico_barras(datos):
    #Obtenemos las categorias y candidatos
    cats = list(datos.keys())
    candidatos = list(datos[cats[0]].keys())

    #Para cada categoria
    for cat in cats:
        colores = ["#003f5c","#58508d","#bc5090","#ff6361","#ffa600"]

        #Creamos un arreglo que tendra todos los datos de positividad de todos los candidatos, uno detras del otro
        datos_totales = []
        #Y un arreglo con la cantidad de oraciones dichas por cada candidato (acumulativo), 
        #para saber donde comienza y termina cada uno
        largos = [0]

        #Creamos las leyendas
        legend_elements = []

        #Para cada candidato
        for candidato in candidatos:
            #Adjuntamos sus datos de positividad a datos_totales
            datos[cat][candidato].sort()
            print("mas positivos")
            print(datos[cat][candidato][0])
            print(datos[cat][candidato][1])
            print(datos[cat][candidato][2])
            print("mas negativos")
            print(datos[cat][candidato][-1])
            print(datos[cat][candidato][-2])
            print(datos[cat][candidato][-3])
            datos_totales += datos[cat][candidato]
            #TODO: checkear que esto este bien
            largos.append(len(datos[cat][candidato]) + largos[-1])      
            #Creamos la linea horizontal de promedio para ese candidato
            plt.hlines(y=np.mean(datos[cat][candidato]), xmin=largos[-2], xmax=largos[-1], linewidth=1, color='black')
            plt.hlines(y=np.median(datos[cat][candidato]), xmin=largos[-2], xmax=largos[-1], linewidth=1, color='blue')

        #Creamos las barras verticales
        barlist = plt.bar(range(len(datos_totales)),datos_totales)

        #Para cada elemento de largos a partir del segundo
        for l in range(1,len(largos)):
            #Obtenemos un color para ese candidato
            c = colores.pop()
            #Y seteamos las barras de ese intervalo en ese color
            for i in range(largos[l-1],largos[l]):
                barlist[i].set_color(c)

            #Agregamos el candidato a la leyenda
            #TODO: comprobar que las leyendas coinciden con candidatos
            legend_elements.append(Patch(facecolor=c, edgecolor=c,label=candidatos[4-len(colores)]))
            

        #Titulo, leyenda, xticks,yticks
        plt.title(str("Sentimientos en categoría "+cat))
        legend_elements.append(Line2D([0], [0], color='black', lw=4,label='Promedio'))
        xticks([i+((len(datos_totales))/10) for i in largos[:-1]], candidatos)
        plt.legend(handles=legend_elements)
        yticks([0,0.5,1], ('Más negativo','Neutro', 'Más Positivo'))

        #Mostramos el grafico
        plt.show()


def grafico_lineas(datos):
    #Obtenemos las categorias y candidatos
    cats = list(datos.keys())
    candidatos = list(datos[cats[0]].keys())

    #Para cada categoria
    for cat in cats:
        legend_elements = []
        colores = ["#003f5c","#58508d","#bc5090","#ff6361","#ffa600"]
        #Para cada candidato
        for candidato in candidatos:
            c = colores.pop()
            x = np.arange(len(datos[cat][candidato]))
            y = datos[cat][candidato]
            plt.plot(x, y, c)
            legend_elements.append(Patch(facecolor=c, edgecolor=c,label=candidatos[4-len(colores)]))

        yticks([0,0.5,1], ('Más negativo','Neutro', 'Más Positivo'))
        plt.legend(handles=legend_elements)
        plt.title(cat)
        plt.show()