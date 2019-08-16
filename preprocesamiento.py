#!/usr/bin/env python
# coding: utf-8

import re, string, unicodedata

# NLTK: kit de herramientas de lenguaje natural
import nltk #https://www.nltk.org/
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from nltk.probability import FreqDist
from nltk import tokenize

#Importar modulo de lectura de pypdf
from PyPDF2 import PdfFileReader

# INFLECT: para realizar las tareas relacionadas con el lenguaje natural de generar plurales, sustantivos singulares, ordinales y artículos indefinidos, y (lo que más nos interesa) convertir números en palabras
import inflect #https://pypi.org/project/inflect/

#Devuelve diccionario procesado con datos del discurso
def leer_archivo():
    #Vamos a leer pdf con el discurso de los 6 candidatos
    discurso_6_candidatos = PdfFileReader(open("datos/Version-taquigrafica.pdf", "rb"))


    #Capturar la cantidad de paginas que tiene el documento
    paginas = discurso_6_candidatos.getNumPages()
    print('Cantidad de páginas:',paginas)


    texto_discurso_6 = ""
    for i in range(paginas):
        pagina_i = discurso_6_candidatos.getPage(i)
        texto_i = pagina_i.extractText()
        texto_discurso_6 = texto_discurso_6 + ' ' + texto_i.replace('\n',"")


    diccionario = dict()
    lista_discurso = texto_discurso_6.split()
    iteraciones = len(lista_discurso)

    for t in range(iteraciones):
        #print(t,lista_discurso[t])
        if lista_discurso[t] == 'Sr.' or lista_discurso[t] == 'Sra.':#Empieza a hablar
            #print(lista_discurso[t],lista_discurso[t+1])
            aux = t + 1
            #print(aux,lista_discurso[aux])
            if '.-' in lista_discurso[aux]:
                candidato = lista_discurso[aux].replace('.-',"")
                aux += 1
            else:
                candidato = lista_discurso[aux] + ' ' + lista_discurso[aux+1].replace('.-',"")
                aux+=2
            if not candidato in diccionario:
                diccionario[candidato] = ""
            while lista_discurso[aux] != 'Sr.' and lista_discurso[aux] != 'Sra.' and aux < iteraciones -1:#Empieza a hablar otro
                try:
                    diccionario[candidato] = diccionario[candidato] + " " + lista_discurso[aux]
                    aux += 1
                except:
                    pass
            t = aux

    #Quito lo que dicen los conductores
    del diccionario['Barili']
    del diccionario['Bonelli']
    del diccionario['Novaresio']

    #Descargar diccionario en csv separado por ;
    with open('dicurso_por_candidato.csv', 'w') as f:
        for key in diccionario.keys():
            f.write("%s;%s\n"%(key,diccionario[key]))

    return diccionario


def leer_archivo_separado():
    #Vamos a leer pdf con el discurso de los 6 candidatos
    discurso_6_candidatos = PdfFileReader(open("datos/Version-taquigrafica.pdf", "rb"))


    #Capturar la cantidad de paginas que tiene el documento
    paginas = discurso_6_candidatos.getNumPages()
    print('Cantidad de páginas:',paginas)


    texto_discurso_6 = ""
    for i in range(paginas):
        pagina_i = discurso_6_candidatos.getPage(i)
        texto_i = pagina_i.extractText()
        texto_discurso_6 = texto_discurso_6 + ' ' + texto_i.replace('\n',"")

    #Los nombres de las categorias estan hardcodeados para reconocerlos en el texto, ya que
    #la libreria que se utiliza para leer pdfs no reconoce el subrayado que los marca como titulos

    #Cada elemento de categorias es una seccion, que contiene:
    #     -el caracter donde comienza (contando el titluo)
    #     -el caracter donde comienza (sin contarlo)
    #     -el caracter donde termina
    #     -el texto que contiene
    #     -el diccionario que se obtendra como resultado del preprocesamiento

    #Ejemplo de uso: categorias["Desarrollo económico y humano"]["Diccionario"]["Macri"]
    nombres_categorias = ["Introducción","Desarrollo económico y humano","Educación e infancia","Seguridad y derechos humanos","Fortalecimiento democrático","Cierre de candidatos"]
    categorias = {}
    for n in nombres_categorias:
        categorias[n] = {"Comienzo_titulo":0, "Comienzo_sec":0,"Fin":0,"Texto":[],"Diccionario":{},"Oraciones":{}}

        #para cada categoria obtenemos comienzos y fin
        categorias[n]["Comienzo_titulo"] = texto_discurso_6.find(n)
        categorias[n]["Comienzo_sec"] = categorias[n]["Comienzo_titulo"] + len(n)
        if n == nombres_categorias[-1]:
            categorias[n]["Fin"] = len(texto_discurso_6) - 1
        else:
            categorias[n]["Fin"] = texto_discurso_6.find(nombres_categorias[nombres_categorias.index(n)+1])-1

        #Obtenemos el campo texto, separando el texto segun los comienzos y fines
        categorias[n]["Texto"] = texto_discurso_6[categorias[n]["Comienzo_sec"]:categorias[n]["Fin"]]

        #Realizamos el preprocesamiento necesario
        t = categorias[n]["Texto"]
        diccionario = dict()
        lista_discurso = t.split()
        iteraciones = len(lista_discurso)

        for t in range(iteraciones):
            #print(t,lista_discurso[t])
            if lista_discurso[t] == 'Sr.' or lista_discurso[t] == 'Sra.':#Empieza a hablar
                #print(lista_discurso[t],lista_discurso[t+1])
                aux = t + 1
                #print(aux,lista_discurso[aux])
                if '.-' in lista_discurso[aux]:
                    candidato = lista_discurso[aux].replace('.-',"")
                    aux += 1
                else:
                    candidato = lista_discurso[aux] + ' ' + lista_discurso[aux+1].replace('.-',"")
                    aux+=2
                if not candidato in diccionario:
                    diccionario[candidato] = ""
                while lista_discurso[aux] != 'Sr.' and lista_discurso[aux] != 'Sra.' and aux < iteraciones -1:#Empieza a hablar otro
                    try:
                        diccionario[candidato] = diccionario[candidato] + " " + lista_discurso[aux]
                        aux += 1
                    except:
                        pass
                t = aux

        #Quito lo que dicen los conductores
        for conductor in ['Barili','Bonelli','Novaresio']:
            if conductor in diccionario:
                del diccionario[conductor]

        #Descargar diccionario en csv separado por ;
        with open('dicurso_por_candidato.csv', 'w') as f:
            for key in diccionario.keys():
                f.write("%s;%s\n"%(key,diccionario[key]))

        categorias[n]["Diccionario"] =  diccionario

        #Separo discurso por oraciones
        for candidato in list(categorias[n]["Diccionario"].keys()):
            categorias[n]["Oraciones"][candidato] =  tokenize.sent_tokenize(categorias[n]["Diccionario"][candidato])

    return categorias


#Normalización
#poner todo el texto en igualdad de condiciones: convirtiendo todo el texto en el
#mismo caso (superior o inferior), eliminando la puntuación, convirtiendo los números
#a sus equivalentes de palabras, y así sucesivamente

def remove_non_ascii(words):
    """Eliminar caracteres no ASCII de la lista de palabras en token"""
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words

def to_lowercase(words):
    """Convierte todos los caracteres a minúsculas de la lista de palabras tokenizadas"""
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words

def remove_punctuation(words):
    """Eliminar puntuación de la lista de palabras tokenizadas"""
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words

def replace_numbers(words):
    """Reemplace todas las apariciones de enteros en la lista de palabras tokenizadas con representación textual"""
    p = inflect.engine()
    new_words = []
    for word in words:
        if word.isdigit():
            new_word = p.number_to_words(word)
            new_words.append(new_word)
        else:
            new_words.append(word)
    return new_words

def remove_stopwords(words):
    """Eliminar palabras de parada de la lista de palabras en token"""
    new_words = []
    for word in words:
        if word not in stopwords.words('english'):
            new_words.append(word)
    return new_words

def stem_words(words):
    """Stem words in list of tokenized words"""
    stemmer = LancasterStemmer()
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems

def lemmatize_verbs(words):
    """Lemmatize verbs in list of tokenized words"""
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return lemmas

def normalize(words):
    words = remove_non_ascii(words)
    words = to_lowercase(words)
    words = remove_punctuation(words)
    words = replace_numbers(words)
    words = remove_stopwords(words)
    return words

def stem_and_lemmatize(words):
    stems = stem_words(words)
    lemmas = lemmatize_verbs(words)
    return stems, lemmas

#Las palabras clave se consideran como ruido en el texto. Las eliminamos
stop_words=set(stopwords.words("spanish"))
