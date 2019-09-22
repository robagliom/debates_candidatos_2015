from matplotlib import pyplot as plt
from nltk.probability import FreqDist
from analisis import tokenizacion
import numpy as np
import operator
from wordcloud import WordCloud

def comparacion_macri_comun(dic1,dic2,modo = "Relativo"):
    for cat in list(dic1.keys())[1:-1]:
        print(cat)
        fdist = [FreqDist(tokenizacion(dic1[cat]["Diccionario"]["Macri"])),FreqDist(tokenizacion(dic2[cat]["Diccionario"]["Macri"]))]
        common_words = [i for i in (list(fdist[0].keys()) + list(fdist[1].keys())) if (i in fdist[0] and i in fdist[1])]
        if modo == "Absoluto":
            resultado = [[i, (fdist[1].get(i) - fdist[0].get(i))] for i in common_words]
        if modo == "Relativo":
            resultado = [[i, ((fdist[1].get(i)/sum(fdist[1].values())) - (fdist[0].get(i)/sum(fdist[0].values())))] for i in common_words]
        #Filtros
        """
        resultado = [i for i in resultado if i[1]!=0]
        res_pos = [i for i in resultado if i[1]>0]
        res_pos = [i for i in res_pos if abs(i[1])>(np.average([abs(i[1]) for i in res_pos]))]
        res_neg = [i for i in resultado if i[1]<0]
        res_neg = [i for i in res_neg if abs(i[1])>(np.average([abs(i[1]) for i in res_neg]))]
        resultado = res_pos+res_neg
        """
        #print(resultado)
        resultado = sorted(resultado, key=operator.itemgetter(1))
        resultado.reverse()
        barlist = plt.bar([i[0] for i in resultado],[i[1] for i in resultado])
        for b in barlist:
            if b.get_height() > 0:
                b.set_color("green")
            else:
                b.set_color("red")
        plt.title(cat)
        plt.xticks(rotation='vertical')
        plt.show()

def palabras_distintas(dic1,dic2):
    for cat in list(dic1.keys())[1:-1]:
        fdist = [tokenizacion(dic1[cat]["Diccionario"]["Macri"]),tokenizacion(dic2[cat]["Diccionario"]["Macri"])]
        unique_words = [None,None]
        unique_words[0] = [i for i in fdist[0] if (i not in fdist[1])]
        unique_words[1] = [i for i in fdist[1] if (i not in fdist[0])]
        print(unique_words[1])
        wc1 = WordCloud(width=1000,height=1000,background_color="White",max_words=150).generate(' '.join((unique_words[0])))
        wc2 = WordCloud(width=1000,height=1000,background_color="White",max_words=150).generate(' '.join((unique_words[1])))
        fig, axeslist = plt.subplots(ncols=2, nrows=1)
        axeslist.ravel()[0].imshow(wc1, cmap=plt.gray())
        axeslist.ravel()[0].set_title("Primer Discurso")
        axeslist.ravel()[0].set_axis_off()
        axeslist.ravel()[1].imshow(wc2, cmap=plt.gray())
        axeslist.ravel()[1].set_title("Segundo Discurso")
        axeslist.ravel()[1].set_axis_off()
        plt.axis("off")
        plt.show()
