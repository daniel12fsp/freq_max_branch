#!/bin/python

from __future__ import print_function
import freq_max_root 
from extraction import extraction_xpath_dir
import info 
import utils

for base in info.all_base()[1:]:
	print(base)
	output = open("../output/xpaths_" + base, "w", 0)
	output.write(base + "\n")
	for i, t in enumerate(utils.combinations_pages(base, info.QTD_PAG)):
		if(i == 100): break
		print(t)
		pages = list(t)
		try:
		#pages = ["/media/doc/home/doc/2014/academico/Pibic/codigos/freq_max_leaf-git/freq_max/../base/abt/62140.html", "/media/doc/home/doc/2014/academico/Pibic/codigos/freq_max_leaf-git/freq_max/../base/abt/78609.html"]
			freq_max_root.rodada(pages, output)
		except: 
			output.write("#Errror")

		#break
	output.close()
	#testar o xpath gerados
	#extraction_xpath_dir(info.path(store), store, info.lca(store))


