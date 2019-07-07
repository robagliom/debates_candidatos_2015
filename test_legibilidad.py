from legibilidad import *
import matplotlib.pyplot as plt

#TEST LEGIBILIDAD CANDIDATOS
def test_legibilidad(diccionario):
    results = {"Macri":{},"Stolbizer":{},"Massa":{},"Del Caño":{},"Rodríguez Saá":{}}

    for key in list(results.keys()):
        results[key]["INFLESZ"] = fernandez_huerta(diccionario[key])
        results[key]["Szigriszt Pazos"] = szigriszt_pazos(diccionario[key])
        results[key]["Gutierrez"] = gutierrez(diccionario[key])
        results[key]["Mu"] = mu(diccionario[key])
        results[key]["Crawford"] = crawford(diccionario[key])

    rows = [key for key in list(results.keys())]
    columns = [key for key in list(results[rows[0]].keys())]
    data = [[0 for i in range(len(columns))] for j in range(len(rows))]

    for r in range(len(rows)):
        for c in range(len(columns)):
            data[r][c] = results[rows[r]][columns[c]]

    fig=plt.figure()
    ax = plt.gca()
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    tbl = ax.table(cellText=data,rowLabels=rows,colLabels=columns,loc='center',colWidths=[0.08 for x in columns])
    tbl.scale(0.6*2,1.5*2)
    plt.title("Comparación de complejidad de textos de todos los candidatos por múltiples métodos")
    plt.show()



    data = []
    columns = []
    for key in list(results.keys()):
        columns.append(key + "\n"+ str(results[key]["INFLESZ"]))
        data.append(results[key]["INFLESZ"])

    plt.figure()
    plt.bar(columns,data)
    plt.title("Análisis de complejidad de texto por método INFLESZ")
    plt.ylim(60,70)
    plt.show()
