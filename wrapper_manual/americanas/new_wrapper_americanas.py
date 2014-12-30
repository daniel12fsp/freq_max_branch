#!/bin/python3
import re
import bs4
from unidecode import unidecode
import json
import os
import glob
import html
import bs4

def normalize(value):
	value = html.unescape(value) #tira as entidades htmls
	value = unidecode(value)# retira os elementos acentuacos(especiais)
	value = re.sub("</?.*?/?>", "", value)
	value = re.sub("\s{2}", "", value)
	value = re.sub("^\s", "", value)
	value = re.sub("\s$", "", value)
	value = re.sub("\[|\]", "", value)
	return value.lower()

def wrapper(filename):
	html =  open(filename, "r", encoding="utf8").read()
	print(filename)
	tree = bs4.BeautifulSoup(html)
	dados = []
	for tag_dl in tree.find_all("dl"):
		for tag_dt in tag_dl.find_all("dt"):
			key = tag_dl.dt.string
			answer = ""
			for not_dl in tag_dt.find_all(re.compile("^((?!dl).)*$")):
				print(not_dl.string)
				answer += str(not_dl.string)
			dados.append((key, answer))
	"""
	result = re.findall(""\"<dl>((.|\s)+?)</dl>""\", html)
	ficha =  result[0][0]
	dados = re.findall("<dt>(.+?)</dt>.*?(<dd.*).*<dl>", ficha, re.S)
	"""
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
	filename = "/media/doc/home/doc/2013/academico/project_antigo/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_base/ponto_frio_notebooks/7031463.html"
	extraction = out_json(filename)
	if(extraction):
		jsao.write(extraction)
	exit()
print("finalizou")
jsao.close()
