#!/bin/python

import os
import re
import os
import glob

folder = "/media/doc/home/doc/2013/academico/project/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_sites/pontofrio_notebooks/" 

new_folder = "/media/doc/home/doc/2013/academico/project/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_sites/pontofrio_notebooks/paginas_estranhas/" 

files = sorted(glob.glob(folder+'*.html'))
for filename in files:
	page =  open(filename, "r").read()
	result = re.findall('(Especificações Técnicas)', page, re.S)
	if(len(result) >= 2):
		id_file =	re.findall("/(\d+\.html)",filename)[0]
		os.rename(filename, new_folder + id_file)
