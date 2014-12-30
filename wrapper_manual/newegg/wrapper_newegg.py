#!/bin/python3
import re
import bs4
from unidecode import unidecode
import json
import os
import glob
#from pdb import set_trace; set_trace()

def wrapper(filename):
	html =  open(filename, "r", encoding="utf8").read()
	print("ARQUIVO: " , filename)
	html = re.sub("<br.*?>","", html)
	result = re.findall("""<dt>(.+?)</dt><dd>(.+?)</dd>""", html)
	return result

	

def out_json(filename):
	dados = wrapper(filename)
	if (dados):
		attrs = {}
		for attr,value in dados:
			attrs[unidecode(attr.lower())] = [unidecode(value.lower())]
		
		id_file =	re.findall("(\d+)\.html", filename)[0]
		return """{"id": %s, "atributos": %s}\n""" % (id_file,json.dumps(attrs, sort_keys=True))


folder = '/media/doc/home/doc/2013/academico/project_antigo/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_base/new_egg_tvs/'
os.listdir(folder)

jsao = open("gabarito_new_egg.json","w")
for filename in glob.glob(folder+'*.html'):
	extraction = out_json(filename)
	if(extraction):
		jsao.write(extraction)
print("finalizou")
jsao.close()
