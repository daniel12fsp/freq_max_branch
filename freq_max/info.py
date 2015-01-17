#!/bin/python
import os

#path
path = os.getcwd() + "/../"
comparator_path = path + "/"
report_path = path + "relatorios/"
base_path = path + "base/"

QTD_PAG = 2

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


def all_base():
	return os.listdir(base_path) 

def is_valid_path(path):
	if(os.path.isdir(path)):
		return path + "/"
	else:
		return None 

"""
abt - 0
adorama - 1
americanas - 2
ao - 3
bhphotovideo - 4
casas_bahia - 5
compsource - 6
crutchfield - 7
cultura - 8
currys - 9
loja_produto.ods - 10
new_egg - 11
overstock - 12
pc_nation - 13
ponto_frio - 14
ricardoeletron - 15
searsoutlet - 16
shopallhome - 17
simples - 18
submarino - 19
"""
