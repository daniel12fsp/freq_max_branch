#!/bin/python
import re
import bs4
from unidecode import unidecode
import json
import os
import glob
import html
import sys

import html


def normalize(value):
	value = html.unescape(value) #tira as entidades htmls
	value = unidecode(value)# retira os elementos acentuacos(especiais)
	return value.lower()

#<div id="descricao" class="descricao">(.|\n)*</div>
def wrapper(filename):
	print(filename)
	page =  open(filename, "r").read()
	result = re.search('<div id="descricao" class="descricao">(.*?)<div id="footer">', page, re.S)
	ficha = result.group(0)
	ficha = re.sub("\s{2,}|\n","", ficha)
	ficha = re.sub("</?br/?>","", ficha)
	ficha = re.sub("</?strong/?>","", ficha)
	dados = re.findall("<dt.*?>(.*?)</dt>.*?<dd.*?>(.*?)</dd>", ficha, re.S)
	for a in dados:
		print(a)
	exit()
	return dados

def out_json(filename):
	
	dados = wrapper(filename)
	attrs = {}
	for attr,value in dados:
		attrs[normalize(attr)] = [normalize(value)]
	
	id_file =	re.findall("/(\d+)\.html",filename)[0]
	return """{"id": %s, "atributos": %s}\n""" % (id_file,json.dumps(attrs, sort_keys=True))


folder = '/media/doc/home/doc/2013/academico/project_antigo/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_base/ponto_frio_notebooks/'

jsao = open("gabarito_ponto_frio.json","w")
files = sorted(glob.glob(folder+'*.html'))

for filename in files:
	filename = "/media/doc/home/doc/2013/academico/project_antigo/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_base/ponto_frio_notebooks/7031463.html"
	jsao.write(out_json(filename))
	exit()
jsao.close()
