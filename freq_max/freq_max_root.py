#!/usr/bin/python3
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
	print("###", big_father)			
	return new_xpaths


def main(path_dir, qtd_max = 10):
	
	pages = utils.list_random_pages(path_dir)[:qtd_max]
	#print(path_dir)
	#print("Qtd de pages", len(pages))
	father = {}
	while(pages != []):
		qtd = 0
		while(qtd < qtd_max and pages != []):
			qtd += 1
			page = pages.pop()
			#print(page)
			ls = utils.prepare(page)
			father = freq_max_root(ls, father)

		xpaths = {}
		for (g, l) in father:
			if(father[(g,l)] < 2):
				if(xpaths.get(g, False)):
					xpaths[g] += round(1.0/(len(l.string)),3)
				else:
					xpaths[g] = 1
					
		#print(xpaths)
		if(father!= {}):
			big_fat = sorted(xpaths.items(), key = lambda x: x[1], reverse=True)
			#print(big_fat[:3])
			#print(">>>", big_fat[0])

		return big_fat[:3]



def rodada(store, output, output2):
	xpaths_finais = {}
	output2.write(store + "\n")
	output.write(store + "\n" )
	for _ in range(10):
		for (xpath, weight) in main(info.base(store)):
				if(xpaths_finais.get(xpath, False)):
					xpaths_finais[xpath] += weight
				else:
					xpaths_finais[xpath] = weight		
	
	big_fat = sorted(xpaths_finais.items(), key = lambda x: x[1], reverse=True)
	output2.write(str(big_fat[:3]) + "\n")
	output2.write("###" + str(big_fat[0]) + "\n")
	output.write(str(big_fat[0]) + "\n" )





