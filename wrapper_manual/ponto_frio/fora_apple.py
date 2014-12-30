import re
from glob import glob
import os

folder = "/media/doc/home/doc/2013/academico/project/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_sites/pontofrio_notebooks/apple/"


for one in glob("*.html"):
	arq = open(one).read()
	resul =	re.search("Apple", arq);
	if(resul):
		print("->>",one)
		os.rename(one, folder+"/"+one)
		print(resul)
