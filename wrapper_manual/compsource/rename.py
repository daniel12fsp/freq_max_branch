#!/bin/python


import os
import bs4
import glob
import re

folder = "/media/doc/home/doc/2013/academico/project_antigo/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_base/compsource_camera/"
#Execute by pypy or python2
for f in glob.glob(folder + "*.htm"):
	html = open(f).read()
	tree_full = bs4.BeautifulSoup(html)
	ident = tree_full.find("title").string.split()[1]
	#print(ident)
	os.rename(f, folder + ident + ".html")

