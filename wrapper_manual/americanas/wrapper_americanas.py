#!/bin/python3
import re
import bs4
from unidecode import unidecode
import json
import os
import glob
import html


def normalize(value):
	value = html.unescape(value) #tira as entidades htmls
	value = unidecode(value)# retira os elementos acentuacos(especiais)
	return value.lower()

def wrapper(filename):
	html =  open(filename, "r", encoding="utf8").read()
	print(filename)
	result = re.findall("""<dl>((.|\s)+?)</dl>""", html)
	ficha =  result[0][0]
	dados = re.findall("<dt>(.+?)</dt>.*?<dd.+?>(.+?)</dd>", ficha, re.S)
	print(dados)
	return dados

	

def out_json(filename):
	dados = wrapper(filename)
	if (dados):
		attrs = {}
		for attr,value in dados:
			attrs[normalize(attr)] = [normalize(value)]
		
		id_file =	re.findall("/(\d+)\.html",filename)[0]
		return """{"id": %s, "atributos": %s}\n""" % (id_file,json.dumps(attrs, sort_keys=True))


#folder = '/media/doc/home/doc/2013/academico/project/Implementacao/Yang-Algoritmos/novo/rtdm-git/paginas_html/ColetaUFAM/ColetaNova/notebooks/submarino_notebook/'
folder = '/media/doc/home/doc/2013/academico/project_antigo/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_base/americanas_notebooks/'
os.listdir(folder)

jsao = open("gabarito_americanas.json","w")
for filename in glob.glob(folder+'*.html'):
	extraction = out_json(filename)
	if(extraction):
		jsao.write(extraction)
print("finalizou")
jsao.close()
