#!/bin/python
from bs4 import BeautifulSoup
import re
import json
import glob
import info
import utils

def extraction(lca, page_target, id_file, file_json):
	i = 0
	attrs = {}
	tag_attr_name = None
	for leaf in utils.prepare(page_target):
		#print(leaf)
		grandpa = leaf.parent.parent
		if(leaf.string and re.search(lca, utils.generate_xpath(grandpa))):
			value_leaf = utils.normalize(leaf)
			if(not tag_attr_name):
				#print("###", leaf.parent.name)
				tag_attr_name = leaf.parent.name

			if(tag_attr_name == leaf.parent.name):
				key = value_leaf
				value_attr = ""	
			else:
				value_attr += value_leaf if value_leaf != None else ""
				#TODO
				#Eu sei que nao eh a melhor opcao,!
				attrs[key] = [value_attr]

	return attrs
		
def extraction_xpath_dir(path_dir, name, lca):
	file_json = open( name + ".json","w")
	for page in sorted(glob.glob(path_dir + '*html*')):
		print(page)
		id_file =	re.findall("(\d+)\.html", page)[0]
		attrs = extraction(lca, page, id_file, file_json)
		file_json.write("""{"id": %s, "atributos": %s}\n""" % (id_file,json.dumps(attrs, sort_keys=True)))
	file_json.close()



key = "new_egg"
extraction_xpath_dir(info.path(key), key, info.lca(key))
