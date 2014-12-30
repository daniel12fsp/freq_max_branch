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
	tables = tree_full.find_all(class_="specTable")
	data = {}
	for table in tables:
		for tr in table.find_all("tr"):
			tds = tr.find_all("td")
			if(tds != []):
				key = tds[0].get_text()
				answer = tds[1].get_text()
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


folder = '/media/doc/home/doc/2013/academico/project_antigo/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_base/bhphotovideo_tvs/'
os.listdir(folder)

jsao = open("gabarito_bhphotovideo.json","w")

for filename in glob.glob(folder + '*.html'):
	j = json_line(filename)
	if(extraction):
		jsao.write(j)

print("finalizou")
jsao.close()
