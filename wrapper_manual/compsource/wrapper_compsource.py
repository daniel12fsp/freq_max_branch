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
	value = re.sub("\s{2}|\n", "", value)
	value = re.sub("</li>", " ", value)
	value = re.sub("</?.*?/?>", "", value)
	value = re.sub("\s{2}|\n", "", value)
	value = re.sub("^\s", "", value)
	value = re.sub("\s$", "", value)
	value = re.sub("\[|\]", "", value)
	return value.lower()


def extraction(filename):

	html = open(filename, encoding="iso-8859-1").read()
	print(filename)
	tree_full = bs4.BeautifulSoup(html)
	table = tree_full.find(class_="eList").find("table")
	data = {}
	for tr in table.find_all("tr"):
		tds = tr.find_all("td")
		if(len(tds) >= 2):
			key = tds[0].get_text()
			answer = tds[1].get_text(" ", strip=True)
			print(key + ":", answer)
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


folder = "/media/doc/home/doc/2013/academico/project_antigo/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_base/compsource_camera/"
os.listdir(folder)

jsao = open("gabarito_compsource.json","w")

for filename in glob.glob(folder + '*.html'):
	filename = "/media/doc/home/doc/2013/academico/project_antigo/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_base/compsource_camera/V204040SU000.html"
	j = json_line(filename)
	if(extraction):
		jsao.write(j)

print("finalizou")
jsao.close()
