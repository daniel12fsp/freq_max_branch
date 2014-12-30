#!/bin/python

import os
import glob
import re

folder = "ops_ja_vendemos/"
pattern = """<span class="msgSemEstoque">ops, já vendemos todo o estoque</span>"""
for path in glob.glob("*html*"):
	print(path)
	page = open(path)
	if(re.search(pattern, page.read())):
		os.rename(path, folder + path);
	page.close()
