#!/bin/python


import os
import bs4
import glob
import re

folder = '/media/doc/home/doc/2013/academico/project_antigo/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_base/casas_bahia_camera/'

for f in glob.glob(folder + "*.html"):
	html = open(f).read()
	tree_full = bs4.BeautifulSoup(html)
	ident = tree_full.find(id="ctl00_Conteudo_hdnIdSkuSelecionado")["value"]
	#print(ident)
	os.rename(f, folder + ident + ".html")

