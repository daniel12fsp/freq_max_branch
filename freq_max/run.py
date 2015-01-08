#!/bin/python

import freq_max_root 
from extraction import extraction_xpath_dir

store = "ponto_frio"

output2 = open("../output/xpaths_" + store, "w", 0)
freq_max_root.rodada(store, output2)
output.close()


#extraction_xpath_dir(info.path(store), store, info.lca(store))

"""

rodada("americanas", output, output2)
exit()
for store in info.paths:
	output2.write(store + "\n")
	output2.write(("-"*40) + "\n")
	output.write(store + "\n" )
	output.write(("-"*40) + "\n" )
	for _ in range(5):
		rodada(store, output, output2)
		gc.collect()
	output.flush()
	output2.flush()

output.close()
output2.close()
"""

