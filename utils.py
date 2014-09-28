#!/bin/python

from bs4 import BeautifulSoup
import re
import random
import glob
import info
import numpy as np


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

def list_random_pages(path_dir):
	pages = glob.glob(path_dir + "*html*")
	random.shuffle(pages)
	return pages

def preparar(page):
	page = remove_tag_re(page)
	tree = html2tree(page)
	leafs = take_leaf(tree)
	return leafs

def dist_str(s1, s2):
	s1 = "r" + s1
	s2 = "r" + s2
	m = len(s1)
	n = len(s2)

	line = np.zeros((n), dtype=np.int)

	for j in xrange(1, n):
		line[j] = line[ j - 1] + 1
	for i in xrange(1, m):
		diagonal = line[0]
		line[0] +=  1
		left = line[0]
		for j in xrange(1, n):
			up = line[j]
			d = up + 1
			a = left + 1
			r = diagonal
			r += 1 if(s1[i] != s2[j]) else 0
			left = min(d, a, r)
			line[j] = left
			diagonal = up

	return line[n - 1]
