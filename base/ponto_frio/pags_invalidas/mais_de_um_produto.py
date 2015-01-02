#!/bin/python

import glob
import re
import os

for fn in glob.glob("*.html"):
	f = open(fn).read()
	quant = len(re.findall("<div id=\"caracteristicas\" class=\"caracteristicasGerais\">", f))
	if(quant > 1):
		print(fn, "pags_invalidas/" + fn)
		os.rename(fn, "pags_invalidas/" + fn)
