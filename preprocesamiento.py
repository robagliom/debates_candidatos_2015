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

    categorias = {"Introducción": {"Comienzo_titulo":0, "Comienzo_sec":0,"Fin":0,"Texto":[],"Diccionario":[]},
                  "Desarrollo económico y humano": {"Comienzo_titulo":0, "Comienzo_sec":0,"Fin":0,"Texto":[],"Diccionario":[]},
                  "Educación e infancia": {"Comienzo_titulo":0, "Comienzo_sec":0,"Fin":0,"Texto":[],"Diccionario":[]},
                  "Seguridad y derechos humanos": {"Comienzo_titulo":0, "Comienzo_sec":0,"Fin":0,"Texto":[],"Diccionario":[]},
                  "Fortalecimiento democrático": {"Comienzo_titulo":0, "Comienzo_sec":0,"Fin":0,"Texto":[],"Diccionario":[]},
                  "Cierre de candidatos": {"Comienzo_titulo":0, "Comienzo_sec":0,"Fin":0,"Texto":[],"Diccionario":[]}}

    #Obtenemos la lista de nombres de categorias
    keys = list(categorias.keys())
    for cat in range(len(keys)):
        #para cada categoria obtenemos comienzos y fin
        nom_cat = keys[cat]
        categorias[nom_cat]["Comienzo_titulo"] = texto_discurso_6.find(nom_cat)
        categorias[nom_cat]["Comienzo_sec"] = categorias[nom_cat]["Comienzo_titulo"] + len(nom_cat)
        if cat == len(categorias) - 1:
            categorias[nom_cat]["Fin"] = len(texto_discurso_6) - 1
        else:
            categorias[nom_cat]["Fin"] = texto_discurso_6.find(keys[cat+1]) - 1

        #Obtenemos el camo textp, separando el texto segun los comienzos y fines
        categorias[nom_cat]["Texto"] = texto_discurso_6[categorias[nom_cat]["Comienzo_sec"]:categorias[nom_cat]["Fin"]]

        #Realizamos el preprocesamiento necesario
        t = categorias[nom_cat]["Texto"]
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

        categorias[nom_cat]["Diccionario"] =  diccionario

    return categorias


#Normalización
#poner todo el texto en igualdad de condiciones: convirtiendo todo el texto en el
#mismo caso (superior o inferior), eliminando la puntuación, convirtiendo los números
#a sus equivalentes de palabras, y así sucesivamente

def remove_non_ascii(words):
    """Eliminar caracteres no ASCII de la lista de palabras en token"""
    new_words = []
    for word in words:
        if 'ñ' in word:
            new_word = word
        else:
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

def remove_adverbios(words):
    print('remove_adverbios')
    with open('lenguaje_español/adverbios.txt', 'r') as f:
        adverbios = [linea.replace('\n','') for linea in f]
    print(adverbios)
    sin_adverbios = []
    for word in words:
        if not word in adverbios:
            sin_adverbios.append(word)
    return sin_adverbios

def remove_conjunciones(words):
    print('remove_conjunciones')
    with open('lenguaje_español/conjunciones.txt', 'r') as f:
        conjunciones = [linea.replace('\n','') for linea in f]
    print(conjunciones)
    sin_conjunciones = []
    for word in words:
        if not word in conjunciones:
            sin_conjunciones.append(word)
    return sin_conjunciones

def remove_preposiciones(words):
    print('remove_preposiciones')
    with open('lenguaje_español/preposiciones.txt', 'r') as f:
        preposiciones = [linea.replace('\n','') for linea in f]
    print(preposiciones)
    sin_preposiciones = []
    for word in words:
        if not word in preposiciones:
            sin_preposiciones.append(word)
    return sin_preposiciones

def normalize(words):
    print('normalize')
    words = remove_non_ascii(words)
    words = to_lowercase(words)
    words = remove_punctuation(words)
    words = replace_numbers(words)
    words = remove_stopwords(words)
    words = remove_adverbios(words)
    words = remove_conjunciones(words)
    words = remove_preposiciones(words)
    return words

def stem_and_lemmatize(words):
    stems = stem_words(words)
    lemmas = lemmatize_verbs(words)
    return stems, lemmas

#Las palabras clave se consideran como ruido en el texto. Las eliminamos
stop_words=set(stopwords.words("spanish"))
