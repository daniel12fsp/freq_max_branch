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
	value = re.sub("\s{2}|\n", "", value)
	value = re.sub("^\s", "", value)
	value = re.sub("\s$", "", value)
	value = re.sub("\[|\]", "", value)
	return value.lower()

def wrapper(filename):
	try:
		html =  open(filename, "r", encoding="utf8").read()
		html = re.sub("</?br/?>", "", html)
		print(filename)
		tree_full = bs4.BeautifulSoup(html)
		tree = tree_full.find(id="ctl00_Conteudo_ctl51_Content")
		dados = []

		for tag_dt in tree.find_all("dt"):
			key = tag_dt.string
			answer = ""
			for not_dl in tag_dt.parent.find_all(text=True, recursive=True)[2:]:#find_all(name=re.compile("^((?!dt).)*$"), recursive=True):
				answer += str(not_dl.string)
			dados.append((key, answer))

		tree = tree_full.find(id="ctl00_Conteudo_ctl51_DetalhesProduto_DimensoesProduto_Content")

		for tag_dt in tree.find_all("dt"):
			dados.append((tag_dt.string, tag_dt.next_sibling.string))
		"""
		result = re.findall(""\"<dl>((.|\s)+?)</dl>""\", html)
		ficha =  result[0][0]
		dados = re.findall("<dt>(.+?)</dt>.*?(<dd.*).*<dl>", ficha, re.S)
		"""
		return dados
	except:
		print("Erro")
		return ""

def out_json(filename):
	dados = wrapper(filename)
	if (dados):
		attrs = {}
		for attr,value in dados:
			attrs[normalize(attr)] = [normalize(value)]
		id_file =	re.findall("/(\d+)\.html",filename)[0]
		return """{"id": %s, "atributos": %s}\n""" % (id_file,json.dumps(attrs, sort_keys=True))


#folder = '/media/doc/home/doc/2013/academico/project/Implementacao/Yang-Algoritmos/novo/rtdm-git/paginas_html/ColetaUFAM/ColetaNova/notebooks/submarino_notebook/'
folder = '/media/doc/home/doc/2013/academico/project_antigo/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_base/ponto_frio_notebooks/'
os.listdir(folder)

jsao = open("gabarito_ponto_frio.json","w")
for filename in glob.glob(folder+'*.html'):
	extraction = out_json(filename)
	if(extraction):
		jsao.write(extraction)
print("finalizou")
jsao.close()
