#!/bin/python

path = "/media/doc/home/doc/2013/academico/project_antigo/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_base/"

paths ={
"new_egg" : path + "new_egg_tvs/",
"ponto_frio" :  path + "ponto_frio_notebooks/",
"abt" : path + "abt_notebooks/",
"americanas" : path +  "americanas_notebooks/",
"submarino" : path + "submarino_smartphones/"
}

lcas ={
"new_egg" : "/fieldset/dl",
"ponto_frio" : "div/div/div/div/div/div/dl",
"abt" :  "/html/body/div/div/div/div/div/ul",
"americanas" : "/div/div/div/div/div/div/dl"

}
comparator_path = "/media/doc/home/doc/2014/academico/outros/freq_max_leaf-git/"

comparator = {
"americanas" : (comparator_path + "json/americanas.json", comparator_path + "gabarito/gabarito_americanas.json"),
"ponto_frio" : (comparator_path + "json/ponto_frio.json", comparator_path + "gabarito/gabarito_ponto_frio.json"),
"new_egg" : (comparator_path + "json/new_egg.json", comparator_path + "gabarito/gabarito_new_egg.json")
}

def lca(key):
	return lcas.get(key)

def path(key):
	return paths.get(key)


