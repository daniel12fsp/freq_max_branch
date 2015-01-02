import re
from glob import glob
import os

folder = "apple/"


for one in glob("*.html"):
	arq = open(one).read()
	resul =	re.search("Apple", arq);
	if(resul):
		print("->>",one)
		os.rename(one, folder+"/"+one)
		print(resul)
