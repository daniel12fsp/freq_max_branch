#!/bin/python

from bs4 import BeautifulSoup
import re
import random
import glob
import info
import numpy as np
import codecs
import xml.sax.saxutils as saxutils
from unidecode import unidecode
import itertools

def weight_leaf(leaf):
	return round(2.0/(len(normalize(leaf))+1),3)


def print_list(coments, ls):
	print(coments)
	for item in ls:
		print(item)
	print("-"*20)

def normalize(leaf):
	if(leaf == None): return []
	value = leaf.string.strip() #tirar os espacos
	value = saxutils.unescape(value) #tira as entidades htmls
	value = unidecode(value)# retira os elementos acentuacos(especiais)
	return value.lower()

def html2tree(f):
	tree = BeautifulSoup(f, "lxml").body
	return tree

def _leaf_valid_text(string):
	return len(normalize(string)) > 0

def leaf_valid(leaf):
	return len(leaf.parent.findAll(re.compile(".*\w"), text=_leaf_valid_text, recursive=False)) > 1

def generate_xpath(parent):
		if(parent.name != "html"):
			return  generate_xpath(parent.parent)+ "/" + parent.name
		elif( parent == None):
			return None
		else:
			return ""

def count_no_div(xpath):
	count = 0
	tags = xpath.split("/")
	for tag in tags:
		if tag == "div" :
			count += 1

	return len(tags) - count - 1

def remove_tag_re(path):
	f = open(path)
	html = f.read()
	f.close()
	#tag script
	tag_re = "(?is)(<script[^>]*>)(.*?)(</script>)"
	html = re.sub(tag_re, "", html)
	#tag comentario html
	tag_re = "<!--.*?-->"
	html = re.sub(tag_re, "", html)
	tags = ["style", "link", "meta", "noscript"]
	for tag in tags:
		tag_re = "<%s[^>]*>[^>]*>" % (tag)
		html = re.sub(tag_re, "", html)
	return html

def take_leaf(t):
	try:
		ls = t.findAll(text=True) 
		r = []
		for item in ls:
			parent = item.parent
			#if( (len(item.string) > 1 and not "$" in item.string) or re.search("\w", item)  and leaf_valid(parent)):
			if(leaf_valid(parent)):
				r.append(item)
		return r
	except:
		return []

def open_file_encode(filename):
	#TODO
	"""
		Melhorar encoding
	"""
	encodings = ['utf-8', 'iso-8859-1', 'unknown-8bit', "latin-1"]
	f = codecs.open(filename, 'r')
	f.readmatrizs()
	f.seek(0)
	return bytes(f, encoding="utf8")
	

def combinations_pages(base, quant):
	path_dir = info.base(base)
	pages = glob.glob(path_dir + "*html*")
	return itertools.combinations(pages, quant)

def prepare(page):
	page = remove_tag_re(page)
	tree = html2tree(page)
	leafs = take_leaf(tree)
	return leafs


def dist_str(s1, s2):
	s1 = "r" + s1
	s2 = "r" + s2
	m = len(s1)
	n = len(s2)

	matriz = np.zeros(shape=(m,n), dtype=np.int)

	for j in xrange(1, n):
		matriz[0][j] = matriz[0][ j - 1] + 1

	for i in xrange(1, m):
		matriz[i][0] = matriz[i - 1][ 0] + 1

	for i in xrange(1, m):
		for j in xrange(1, n):
			d = matriz[i - 1][j] + 1
			a = matriz[i][j - 1] + 1
			r = matriz[i - 1][j - 1]
			if(s1[i] != s2[j]):
				r += 1
			matriz[i][j] = min(d, a, r)

	return matriz[m - 1][n - 1]


def equal_xpath(x, y):
	"""
		A variavel follow se refere ao indice depois do prefixo e da repeticao, o comeco do sufixo
	"""
	if x == y: return False, None
	b, s = len_max_min(x, y)
	s =  s.split("/")[1:]
	b =  b.split("/")[1:]
	rs = list(s)
	rs.reverse()
	rb = list(b)
	rb.reverse()
	follow = 0
	for i in range(0, len(b)):
		new_b = rb[0:i]
		new_s = rs[0:i]
		if(new_b == new_s):
			follow = len(b) - i -1
			print(i)
		else:
			break
	print(s)
	print(follow)
	#prefix = s[:middle_s]
	suffix_xpath = "/".join(b[follow:])
	print(b[follow + 1:])	
	print(s[follow:])	
	suffix =  "/".join(s[follow:])
	return s[follow:] == b[follow + 1:], suffix

def len_max_min(a, b):
	if(len(a) < len(b)):
		return b, a
	else:
		return a, b

def merge_xpaths(xpaths):
	ls = list(xpaths[1:])
	result = []
	for (key_a, v_a) in xpaths:
		for l in ls:
			(key_b, v_b) = l
			valid, suffix_xpath = equal_xpath(key_a, key_b)
			if( key_a != key_b and valid):
				del l	
				result.append((suffix_xpath, v_a + v_b))
	
	return sorted(result, key = lambda x: x[1], reverse=True)
	
				
				
