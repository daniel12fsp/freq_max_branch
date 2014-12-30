#!/bin/python3
import re
import os
import shutil
import glob

def isValidationPage(page):
	html = open(page,"r").read()
	result = re.findall("""<dl>(.+?)</dl>""", html, re.S)
	#result = re.search("""<title>Notebook(.*?)</title>""", html, re.S)
	#print(result)
	return result
folder = '/home/ervili/rtdm/teste/americanas_notebooks/notebooks  - Pages/'
newFolder = '/home/ervili/rtdm/teste/americanas_notebooks/notebooks/'
os.listdir(folder)
for filename in glob.glob(folder+'*.html'):
	print("\nPAGE: " + filename)
	if(isValidationPage(filename)):
		print(filename + " movido")
		shutil.copy2(filename,newFolder)
		

	


