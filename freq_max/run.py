#!/bin/python

import freq_max_root 
from extraction import extraction_xpath_dir
import info 

for base in info.all_base():
	base = "ponto_frio"
	output2 = open("../output/xpaths_" + base, "w", 0)
	freq_max_root.rodada(base, output2)
	output2.close()
	exit()
	#testar o xpath gerados
	#extraction_xpath_dir(info.path(store), store, info.lca(store))


