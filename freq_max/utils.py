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

def normalize(leaf):
	value = leaf.string.strip() #tirar os espacos
	value = saxutils.unescape(value) #tira as entidades htmls
	value = unidecode(value)# retira os elementos acentuacos(especiais)
	return value.lower()

def html2tree(f):
	tree = BeautifulSoup(f,"lxml").body
	return tree

def leaf_valid(parent):
	return len(parent.parent.findAll(re.compile(".*\w"), text=True, recursive=False)) > 1

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
	ls = t.findAll(text=True) 
	r = []
	for item in ls:
		parent = item.parent
		if( (len(item.string) > 1 and not "$" in item.string) or re.search("\w", item)  and leaf_valid(parent)):
			r.append(item)
	return r

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
	

def list_random_pages(path_dir):
	pages = glob.glob(path_dir + "*html*")
	random.shuffle(pages)
	return pages

def prepare(page):
	try:
		page = remove_tag_re(page)
		tree = html2tree(page)
		leafs = take_leaf(tree)
		return leafs
	except:
		return []	

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