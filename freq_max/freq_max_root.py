#s1!/usr/bin/python3
# -*- coding: utf8 -*-
import info
import utils
import re
import gc


def freq_max_root(page, father, output):
	output.write("\n" + page)
	ls = utils.prepare(page)
	for leaf in ls:
		grandpa = leaf.parent.parent
		xpath_grandpa = utils.generate_xpath(grandpa)
		if father.get((xpath_grandpa, leaf)) == None:
			father[(xpath_grandpa, leaf)] = 1 
		else: 
			father[(xpath_grandpa, leaf)] += 1
	#print(father)
	return father


def main(pages, output):
	
	father = {}
	for page in pages:
		father = freq_max_root(page, father, output)
		#print(len(father))
		#utils.print_list("Father", father.items())
		xpaths = {}
		for (g, l) in father:
			if(xpaths.get(g, False)):
				xpaths[g] += utils.weight_leaf(l) 
			else:
				xpaths[g] = 1
	return xpaths.items()


def rodada(pages, output):
	xpaths_finais = {}
	for (xpath, weight) in main(pages, output):
			if(xpaths_finais.get(xpath, False)):
				xpaths_finais[xpath] += weight
			else:
				xpaths_finais[xpath] = weight		
	big_fat = sorted(xpaths_finais.items(), key = lambda x: x[1], reverse=True)
	if __debug__:
		utils.print_list("big_fat", big_fat)
	chooses_ones = big_fat[:5]
	#the_choose_one = utils.merge_xpaths(chooses_ones)
	#output.write("\n"+ "M>" + str(the_choose_one))
	output.write("\n"+ "N^" + str(chooses_ones[0]))

	output.write("\n" + "#"*30)
