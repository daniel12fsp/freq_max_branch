#!/bin/python


import os
import bs4
import glob

folder = '/media/doc/home/doc/2013/academico/project_antigo/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_base/adorama_notebooks/'

for f in glob.glob(folder + "*.html"):
	html = open(f).read()
	tree_full = bs4.BeautifulSoup(html)
	sku = tree_full.find(attrs={'itemprop': "sku"}).string
	os.rename(f, folder + sku + ".html")
