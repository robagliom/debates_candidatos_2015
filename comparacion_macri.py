from matplotlib import pyplot as plt
from nltk.probability import FreqDist
from analisis import tokenizacion
import operator

def comparacion_macri(dic1,dic2,modo = "Relativo"):
    for cat in list(dic1.keys())[1:-1]:
        print(cat)
        fdist = [FreqDist(tokenizacion(dic1[cat]["Diccionario"]["Macri"])),FreqDist(tokenizacion(dic2[cat]["Diccionario"]["Macri"]))]
        common_words = [i for i in (list(fdist[0].keys()) + list(fdist[1].keys())) if (i in fdist[0] and i in fdist[1])]
        if modo == "Absoluto":
            resultado = [[i, (fdist[1].get(i) - fdist[0].get(i))] for i in common_words]
        if modo == "Relativo":
            resultado = [[i, ((fdist[1].get(i)/sum(fdist[1].values())) - (fdist[0].get(i)/sum(fdist[0].values())))] for i in common_words]
        resultado = [i for i in resultado if i[1]!=0]
        print(resultado)
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