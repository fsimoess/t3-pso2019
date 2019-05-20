#!/usr/bin/env python3

import sys
import json
import requests
import os


def return_dir():
	path = './'
	diretorio = os.listdir(path)
	diretorio = sorted(diretorio)
	return diretorio

def find_position_folder(image_name, diretorio, pos):
	for num in range(0,len(diretorio)):
		x = diretorio[num]
		if x[-4:] == ".png":
			if image_name == diretorio[num]:
				pos.remove(num)

	return pos

def delete(pos):
	for i in pos:
		x = diretorio[i]
		if x[-4:] == ".png":
			os.remove(diretorio[i])

url = 'http://xkcd.com/info.0.json'
teste = requests.get(url)
teste.raise_for_status()

data = json.loads(teste.text)

diretorio = return_dir()
pos = [i for i in range(0,len(diretorio))] #Lista de Posições dos Arquivos no Diretório

for num in range(data['num']-3, data['num']+1):
	url = 'http://xkcd.com/'+str(num)+'/info.0.json'

	teste = requests.get(url)
	teste.raise_for_status()
	img_data = json.loads(teste.text)

	img = requests.get(img_data['img']).content #pega a imagem

	image_name = str(num)+'-'+img_data['safe_title']+'.png' #string auxiliar para pegar o nome do arquivo
	print(image_name)
	image_name = image_name.replace('/','')
	print(image_name)

	pos = find_position_folder(image_name, diretorio, pos)

	with open(image_name, 'wb') as handler:
			handler.write(img)

delete(pos)
