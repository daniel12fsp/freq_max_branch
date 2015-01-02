#!/bin/python
import os
import utils

#path
path = os.getcwd() + "/../"
comparator_path = path + "/"
report_path = path + "relatorios/"
base_path = path + "base/"

#function returns the paths
def base(store):
	return is_valid_path(base_path + store)

def lca(key):
	return None

def path(key):
	return None#paths.get(key)

def json(key):
	return None#comparator.get(key,(None, None))[0]

def gabarito(key):
	return None#comparator.get(key,(None, None))[1]

def is_valid_path(path):
	print(path)
	if(os.path.isdir(path)):
		return path + "/"
	else:
		return None 
