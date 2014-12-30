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


def extraction(filename):

	html = open(filename).read()
	print(filename)
	tree_full = bs4.BeautifulSoup(html)
	dls = tree_full.find(id="detalhes").find_all("dl")
	data = {}
	for dl in dls:

		key = dl.dt.get_text()
		answer = dl.dd.get_text()
		print(key, answer)
		data[key] = answer

		if(len(dl.find_all("dt")) > 1):
			print("Extraction")
			for dt in dl.find_all("dt")[1:]:
				key = dt.get_text()
				answer = dt.find_next_sibling().get_text()
				print(key, answer)
				data[key] = answer

	return data

def json_line(filename):
	dados = extraction(filename)
	print(dados)
	if (dados):
		attrs = {}
		for attr,value in dados.items():
			attrs[normalize(attr)] = [normalize(value)]	
		id_file =	re.findall(".*/(.*?)\.html",filename)[0]
		return """{"id": "%s", "atributos": %s}\n""" % (id_file,json.dumps(attrs, sort_keys=True))


folder = '/media/doc/home/doc/2013/academico/project_antigo/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_base/casas_bahia_camera/'
os.listdir(folder)

jsao = open("gabarito_casas_bahia.json","w")

for filename in glob.glob(folder + '*.html'):
	j = json_line(filename)
	if(extraction):
		jsao.write(j)

print("finalizou")
jsao.close()
