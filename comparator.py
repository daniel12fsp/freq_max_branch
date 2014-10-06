#!/bin/python
import itertools
import json
import sys
import info

store = "ponto_frio"

lines_experimento = open(info.json(store)).read().splitlines()
print(info.json(store))
lines_gabarito    = open(info.gabarito(store)).read().splitlines()
print(info.gabarito(store))

erro = 0
def float_division(a, b):
	try:
		return a / float(b)
	except:
		return float(0)

precisao_geral = 0
revocacao_geral = 0

def lines_to_hash(lines):
	answer = {}
	for line in lines:
		pag = json.loads(line)
		answer[pag["id"]] = pag
	return answer

experimento = lines_to_hash(lines_experimento )
gabarito    = lines_to_hash(lines_gabarito)


for gab_id in gabarito:

	exp = experimento[gab_id]
	#print(exp)
	gab = gabarito[gab_id]
	#print(gab)
	attr_exp = exp["atributos"]
	attr_gab = gab["atributos"]

	acertos = 0

	for one_attr in attr_gab.keys():
		if(attr_exp.get(one_attr, False) and attr_gab.get(one_attr, False)  and attr_exp[one_attr] == attr_gab[one_attr]):	
			acertos += 1

	precisao = float_division(acertos, len(attr_exp))
	revocacao = float_division(acertos, len(attr_gab))

	precisao_geral += precisao
	revocacao_geral += revocacao

	print("id:%9s, acertos:%2d, precisao:%3f, revocacao:%3f, len attr_pag(experimento):%2d, len attr_gab(gab):%d, %s" 
		% (gab['id'], acertos, precisao, revocacao, len(attr_exp), len(attr_gab), str(exp['id']==gab['id'])))

precisao_final = float_division(precisao_geral, len(gabarito))
revocacao_final = float_division(revocacao_geral, len(gabarito))
print("Informações Gerais")
print("Precisao", precisao_final )
print("Revocacao", revocacao_final)
f1=(2*revocacao_final*precisao_final)/(precisao_final + revocacao_final)
print("f1",f1)
