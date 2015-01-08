#s1!/usr/bin/python3
# -*- coding: utf8 -*-
import info
import utils
import re
import gc


def freq_max_root(ls, father = {}):
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
	utils.print_list("Pages", pages)
	father = {}
	for page in pages:
		ls = utils.prepare(page)
		father = freq_max_root(ls, father)
		utils.print_list("Father", father.items())
	xpaths = {}
	for (g, l) in father:
		if(father[(g,l)] < 2):
			if(xpaths.get(g, False)):
				xpaths[g] += utils.weight_leaf(l) 
			else:
				xpaths[g] = 1
		exit()		
	return xpaths



def rodada(store, output):
	xpaths_finais = {}
	output.write(store + "\n")
	for _ in range(1):
		for (xpath, weight) in main(info.base(store)).items():
				if(xpaths_finais.get(xpath, False)):
					xpaths_finais[xpath] += weight
				else:
					xpaths_finais[xpath] = weight		
	big_fat = sorted(xpaths_finais.items(), key = lambda x: x[1], reverse=True)
	output.write("#"*30)
	for f in big_fat[:3]:
		output.write("\n" + str(f))





"""
def merge_xpath(xpaths):
	new_xpaths = {}
	xpaths_order = sorted(xpaths.keys(), key = lambda x: len(x[0]) )
	for i in range(len(xpaths_order)):
		if(utils.count_no_div(xpaths_order[i]) > 2):
			for xpath in xpaths_order:
				dist_str = utils.dist_str(xpaths_order[i], xpath)
				if( utils.count_no_div(xpath) > 2  and dist_str != 0 and dist_str < 10):
					xpaths[xpaths_order[i]] += xpaths[xpath]
					xo = len(xpaths_order[i])
					xp = len(xpath)
					if(xo < xp):
						least = xpaths_order[i]
					else:
						least = xpath
					if(new_xpaths.get(least, None) == None):
						new_xpaths[least] = xpaths[xpaths_order[i]]



	big_father = max(new_xpaths.items(), key = lambda x: x[1])
	#print(new_xpaths)
	#print("###X.", big_father)			
	return new_xpaths
"""
