#s1!/usr/bin/python3
# -*- coding: utf8 -*-
import info
import utils
import re
import gc


def freq_max_root(page, father):
	print(page)
	ls = utils.prepare(page)
	for leaf in ls:
		grandpa = leaf.parent.parent
		xpath_grandpa = utils.generate_xpath(grandpa)
		if father.get((xpath_grandpa, leaf)) == None:
			father[(xpath_grandpa, leaf)] = 1 
		else: 
			father[(xpath_grandpa, leaf)] += 1
	return father


def main(path_dir, qtd_max = 10):
	
	pages = utils.list_random_pages(path_dir)[:qtd_max]
	#utils.print_list("Pages", pages)
	father = {}
	for page in pages:
		father = freq_max_root(page, father)
		#utils.print_list("Father", father.items())
		xpaths = {}
		for (g, l) in father:
			if(father[(g,l)] < qtd_max + 1):
				if(xpaths.get(g, False)):
					xpaths[g] += utils.weight_leaf(l) 
				else:
					xpaths[g] = 1
	return xpaths


def rodada(base, output):
	xpaths_finais = {}
	output.write(base + "\n")
	for _ in range(1):
		for (xpath, weight) in main(info.base(base)).items():
				if(xpaths_finais.get(xpath, False)):
					xpaths_finais[xpath] += weight
				else:
					xpaths_finais[xpath] = weight		
	big_fat = sorted(xpaths_finais.items(), key = lambda x: x[1], reverse=True)
	output.write("#"*30)
	chooses_ones = big_fat[:5]
	the_choose_one = chooses_ones[1]
	print(the_choose_one)
	print(the_choose_one[0])
	#output.write(utils.merge_xpaths(big_fat[:5]))
