import pygame
import time
from random import randint
import sys
blanco  = (255,255,255) 
def display_mensaje(texto,ventana):
	texto_largo = pygame.font.Font("freesansbold.ttf",115)
	text_surf,text_rect = text_objects(texto,texto_largo)
	text_rect.center = (800/2,600/2)
	ventana.blit(text_surf,text_rect)
	pygame.display.update()
	time.sleep(2)

def text_objects(text,font):
	text_surface = font.render(text,True,blanco)
	return text_surface,text_surface.get_rect()
def multi_novato():
	ins = ["Gira","Golpea","Jala","Pasala"]
	pygame.init()
	ventana = pygame.display.set_mode((800,600))
	pygame.display.set_caption("Bop it")
	reloj = pygame.time.Clock()
	correcto = True
	inicio = time.time()
	chido=0
	while time.time()-inicio< 3  and chido<3:
		time.sleep(3)
		i = randint(0,3)
		display_mensaje(ins[i],ventana)
		ventana.fill((0,0,0))
		if(i==2):
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
					display_mensaje("Correcto",ventana)
					ventana.fill((0,0,0))
					correcto = True
					inicio = time.time()
					chido+=1
				"""else:
					display_mensaje("Ya valiste",ventana)
					ventana.fill((0,0,0))
					correcto = False"""
		if(i==1):		
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					display_mensaje("Correcto",ventana)
					ventana.fill((0,0,0))
					correcto = True
					inicio = time.time()
					chido+=1
				"""else:
					display_mensaje("Ya valiste",ventana)
					ventana.fill((0,0,0))
					correcto = False"""
		if(i==0):
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN and (event.button == 4 or event.button==5):
					display_mensaje("Correcto",ventana)
					ventana.fill((0,0,0))
					correcto = True
					inicio = time.time()
					chido+=1
				"""else:
					display_mensaje("Ya valiste",ventana)
					ventana.fill((0,0,0))
					correcto = False"""
		if(i==3):
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
					display_mensaje("Correcto",ventana)
					ventana.fill((0,0,0))
					correcto = True
					inicio = time.time()
					chido+=1
				"""else:
					display_mensaje("Ya valiste",ventana)
					ventana.fill((0,0,0))
					correcto = False"""

	if chido>=3:
		print("Felicidades")
	else:
		display_mensaje("Ya valiste",ventana)
		ventana.fill((0,0,0))
	pygame.display.quit()
	pygame.quit()
	return chido

def multi_experto():
	ins = ["Gira","Golpea","Jala","Pasala","1","2","3"]
	pygame.init()
	ventana = pygame.display.set_mode((800,600))
	pygame.display.set_caption("Bop it")
	reloj = pygame.time.Clock()
	correcto = True
	inicio = time.time()
	chido=0
	while time.time()-inicio< 3  and chido<3:
		time.sleep(2)
		i = randint(0,6)
		display_mensaje(ins[i],ventana)
		ventana.fill((0,0,0))
		if(i==2):
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
					display_mensaje("Correcto",ventana)
					ventana.fill((0,0,0))
					correcto = True
					inicio = time.time()
					chido+=1
				"""else:
					display_mensaje("Ya valiste",ventana)
					ventana.fill((0,0,0))
					correcto = False"""
		if(i==1):		
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					display_mensaje("Correcto",ventana)
					ventana.fill((0,0,0))
					correcto = True
					inicio = time.time()
					chido+=1
				"""else:
					display_mensaje("Ya valiste",ventana)
					ventana.fill((0,0,0))
					correcto = False"""
		if(i==0):
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN and (event.button == 4 or event.button==5):
					display_mensaje("Correcto",ventana)
					ventana.fill((0,0,0))
					correcto = True
					inicio = time.time()
					chido+=1
				"""else:
					display_mensaje("Ya valiste",ventana)
					ventana.fill((0,0,0))
					correcto = False"""
		if(i==3):
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
					display_mensaje("Correcto",ventana)
					ventana.fill((0,0,0))
					correcto = True
					inicio = time.time()
					chido+=1
				"""else:
					display_mensaje("Ya valiste",ventana)
					ventana.fill((0,0,0))
					correcto = False"""
		if(i==4):
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN and (event.button == 4 or event.button==5):
					display_mensaje("Correcto",ventana)
					ventana.fill((0,0,0))
					correcto = True
					inicio = time.time()
					chido+=1
		if(i==5):
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					display_mensaje("Correcto",ventana)
					ventana.fill((0,0,0))
					correcto = True
					inicio = time.time()
					chido+=1
		if(i==6):
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
					display_mensaje("Correcto",ventana)
					ventana.fill((0,0,0))
					correcto = True
					inicio = time.time()
					chido+=1

	if chido>=3:
		print("Felicidades")
	else:
		display_mensaje("Ya valiste",ventana)
		ventana.fill((0,0,0))
	pygame.display.quit()
	pygame.quit()
	return chido

def solo_master():
	ins = ["Gira","Golpea","Jala","1","2","3",(255,255,0),(255,255,255),(0,0,255)]
	pygame.init()
	ventana = pygame.display.set_mode((800,600))
	pygame.display.set_caption("Bop it")
	reloj = pygame.time.Clock()
	correcto = True
	inicio = time.time()
	chido=0
	while time.time()-inicio< 1 and chido<3:
		time.sleep(1)
		i = randint(0,8)
		if 0<=i<=5:
			display_mensaje(ins[i],ventana)
			ventana.fill((0,0,0))
			if(i==2):
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
						display_mensaje("Correcto",ventana)
						ventana.fill((0,0,0))
						correcto = True
						inicio = time.time()
						chido+=1
					"""else:
						display_mensaje("Ya valiste",ventana)
						ventana.fill((0,0,0))
						correcto = False"""
			if(i==1):		
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
						display_mensaje("Correcto",ventana)
						ventana.fill((0,0,0))
						correcto = True
						inicio = time.time()
						chido+=1
					"""else:
						display_mensaje("Ya valiste",ventana)
						ventana.fill((0,0,0))
						correcto = False"""
			if(i==0):
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN and (event.button == 4 or event.button==5):
						display_mensaje("Correcto",ventana)
						ventana.fill((0,0,0))
						correcto = True
						inicio = time.time()
						chido+=1
					"""else:
						display_mensaje("Ya valiste",ventana)
						ventana.fill((0,0,0))
						correcto = False"""
			if(i==3):
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN and (event.button == 4 or event.button==5):
						display_mensaje("Correcto",ventana)
						ventana.fill((0,0,0))
						correcto = True
						inicio = time.time()
						chido+=1
			if(i==4):
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
						display_mensaje("Correcto",ventana)
						ventana.fill((0,0,0))
						correcto = True
						inicio = time.time()
						chido+=1
			if(i==5):
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
						display_mensaje("Correcto",ventana)
						ventana.fill((0,0,0))
						correcto = True
						inicio = time.time()
						chido+=1
		else:
			ventana.fill(ins[i])
			pygame.display.update()
			time.sleep(1)
			ventana.fill((0,0,0))
			pygame.display.update()
			if(i==6):
				
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN and (event.button == 4 or event.button==5):
						display_mensaje("Correcto",ventana)
						ventana.fill((0,0,0))
						correcto = True
						inicio = time.time()
						chido+=1
			if(i==7):
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
						display_mensaje("Correcto",ventana)
						ventana.fill((0,0,0))
						correcto = True
						inicio = time.time()
						chido+=1
			if(i==8):
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
						ventana.fill((0,0,0))
						pygame.display.update()
						display_mensaje("Correcto",ventana)
						ventana.fill((0,0,0))
						correcto = True
						inicio = time.time()
						chido+=1

	if chido>=3:
		print("Felicidades")
	else:
		display_mensaje("Ya valiste",ventana)
		ventana.fill((0,0,0))
	pygame.display.quit()
	pygame.quit()
	return chido


def multi_master():
	ins = ["Gira","Golpea","Jala","1","2","3","Pasala",(255,255,0),(255,255,255),(0,0,255)]
	pygame.init()
	ventana = pygame.display.set_mode((800,600))
	pygame.display.set_caption("Bop it")
	reloj = pygame.time.Clock()
	correcto = True
	inicio = time.time()
	chido=0
	while time.time()-inicio< 1 and chido<3:
		time.sleep(1)
		i = randint(0,9)
		if 0<=i<=6:
			display_mensaje(ins[i],ventana)
			ventana.fill((0,0,0))
			if(i==2):
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
						display_mensaje("Correcto",ventana)
						ventana.fill((0,0,0))
						correcto = True
						inicio = time.time()
						chido+=1
					"""else:
						display_mensaje("Ya valiste",ventana)
						ventana.fill((0,0,0))
						correcto = False"""
			if(i==1):		
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
						display_mensaje("Correcto",ventana)
						ventana.fill((0,0,0))
						correcto = True
						inicio = time.time()
						chido+=1
					"""else:
						display_mensaje("Ya valiste",ventana)
						ventana.fill((0,0,0))
						correcto = False"""
			if(i==0):
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN and (event.button == 4 or event.button==5):
						display_mensaje("Correcto",ventana)
						ventana.fill((0,0,0))
						correcto = True
						inicio = time.time()
						chido+=1
					"""else:
						display_mensaje("Ya valiste",ventana)
						ventana.fill((0,0,0))
						correcto = False"""
			if(i==3):
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN and (event.button == 4 or event.button==5):
						display_mensaje("Correcto",ventana)
						ventana.fill((0,0,0))
						correcto = True
						inicio = time.time()
						chido+=1
			if(i==4):
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
						display_mensaje("Correcto",ventana)
						ventana.fill((0,0,0))
						correcto = True
						inicio = time.time()
						chido+=1
			if(i==5):
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
						display_mensaje("Correcto",ventana)
						ventana.fill((0,0,0))
						correcto = True
						inicio = time.time()
						chido+=1
			if(i==6):
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
						display_mensaje("Correcto",ventana)
						ventana.fill((0,0,0))
						correcto = True
						inicio = time.time()
						chido+=1
		else:
			ventana.fill(ins[i])
			pygame.display.update()
			time.sleep(1)
			ventana.fill((0,0,0))
			pygame.display.update()
			if(i==7):
				
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN and (event.button == 4 or event.button==5):
						display_mensaje("Correcto",ventana)
						ventana.fill((0,0,0))
						correcto = True
						inicio = time.time()
						chido+=1
			if(i==8):
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
						display_mensaje("Correcto",ventana)
						ventana.fill((0,0,0))
						correcto = True
						inicio = time.time()
						chido+=1
			if(i==9):
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
						ventana.fill((0,0,0))
						pygame.display.update()
						display_mensaje("Correcto",ventana)
						ventana.fill((0,0,0))
						correcto = True
						inicio = time.time()
						chido+=1

	if chido>=3:
		print("Felicidades")
	else:
		display_mensaje("Ya valiste",ventana)
		ventana.fill((0,0,0))
	pygame.display.quit()
	pygame.quit()
	return chido
def solo_experto():
	ins = ["Gira","Golpea","Jala","1","2","3"]
	pygame.init()
	ventana = pygame.display.set_mode((800,600))
	pygame.display.set_caption("Bop it")
	reloj = pygame.time.Clock()
	correcto = True
	inicio = time.time()
	chido=0
	while time.time()-inicio< 2 and chido<3:
		time.sleep(2)
		i = randint(0,5)
		display_mensaje(ins[i],ventana)
		ventana.fill((0,0,0))
		if(i==2):
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
					display_mensaje("Correcto",ventana)
					ventana.fill((0,0,0))
					correcto = True
					inicio = time.time()
					chido+=1
				"""else:
					display_mensaje("Ya valiste",ventana)
					ventana.fill((0,0,0))
					correcto = False"""
		if(i==1):		
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					display_mensaje("Correcto",ventana)
					ventana.fill((0,0,0))
					correcto = True
					inicio = time.time()
					chido+=1
				"""else:
					display_mensaje("Ya valiste",ventana)
					ventana.fill((0,0,0))
					correcto = False"""
		if(i==0):
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN and (event.button == 4 or event.button==5):
					display_mensaje("Correcto",ventana)
					ventana.fill((0,0,0))
					correcto = True
					inicio = time.time()
					chido+=1
				"""else:
					display_mensaje("Ya valiste",ventana)
					ventana.fill((0,0,0))
					correcto = False"""
		if(i==3):
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN and (event.button == 4 or event.button==5):
					display_mensaje("Correcto",ventana)
					ventana.fill((0,0,0))
					correcto = True
					inicio = time.time()
					chido+=1
		if(i==4):
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					display_mensaje("Correcto",ventana)
					ventana.fill((0,0,0))
					correcto = True
					inicio = time.time()
					chido+=1
		if(i==5):
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
					display_mensaje("Correcto",ventana)
					ventana.fill((0,0,0))
					correcto = True
					inicio = time.time()
					chido+=1					
	if chido>=3:
		print("Felicidades")
	else:
		display_mensaje("Ya valiste",ventana)
		ventana.fill((0,0,0))
	pygame.display.quit()
	pygame.quit()
	return chido


def solo():
	ins = ["Gira","Golpea","Jala"]
	pygame.init()
	ventana = pygame.display.set_mode((800,600))
	pygame.display.set_caption("Bop it")
	reloj = pygame.time.Clock()
	correcto = True
	inicio = time.time()
	chido=0
	while time.time()-inicio< 3 and chido<3:
		time.sleep(3)
		i = randint(0,2)
		display_mensaje(ins[i],ventana)
		ventana.fill((0,0,0))
		if(i==2):
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
					display_mensaje("Correcto",ventana)
					ventana.fill((0,0,0))
					correcto = True
					inicio = time.time()
					chido+=1
				"""else:
					display_mensaje("Ya valiste",ventana)
					ventana.fill((0,0,0))
					correcto = False"""
		if(i==1):		
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					display_mensaje("Correcto",ventana)
					ventana.fill((0,0,0))
					correcto = True
					inicio = time.time()
					chido+=1
				"""else:
					display_mensaje("Ya valiste",ventana)
					ventana.fill((0,0,0))
					correcto = False"""
		if(i==0):
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN and (event.button == 4 or event.button==5):
					display_mensaje("Correcto",ventana)
					ventana.fill((0,0,0))
					correcto = True
					inicio = time.time()
					chido+=1
				"""else:
					display_mensaje("Ya valiste",ventana)
					ventana.fill((0,0,0))
					correcto = False"""
	if chido>=3:
		print("Felicidades")
	else:
		display_mensaje("Ya valiste",ventana)
		ventana.fill((0,0,0))
	pygame.display.quit()
	pygame.quit()
	return chido




chido = 0
muln = 0
soloe=0
mule=0
solom = 0
mulm = 0
print("Bienvenido al excitante juego BOP IT!!\nSelecciona modo de juego:")
print("1.- Solo")
print("2.- Multijugador")
modo = int(input())
if modo==1:
	chido = solo()
else:
	muln = multi_novato()
if chido>=3 or muln>=3:
	print("Felicidades Nivel Desblqueado")
	while modo!=3 or soloe<3 or mule<3: 
		print("Bienvenido al excitante juego BOP IT!!\nSelecciona modo de juego:")
		print("1.- Solo")
		print("2.- Multijugador")
		print("3.- Salir :c")
		modo = int(input())
		print("Nivel de dificultad:\n1.-Novato\n2.-Experto")
		nivel = int(input())
		print(modo,nivel)
		if modo == 1 and nivel==1:
			inutil = solo()
		elif modo == 2 and nivel ==1:
			muln = multi_novato()
		elif modo == 1 and nivel==2:
			soloe = solo_experto()
		elif modo==2 and nivel==2:
			mule = multi_experto()
		else:
			break
		if(modo==3 or soloe>=3 or mule>=3):
			break
if soloe>=3 or mule>=3:
	print("Felicidades has desbloqueado todos los niveles!!!!")
	while modo!=3:
		print("Bienvenido al excitante juego BOP IT!!\nSelecciona modo de juego:")
		print("1.- Solo")
		print("2.- Multijugador")
		print("3.- Salir :c")
		modo = int(input())
		print("Nivel de dificultad:\n1.-Novato\n2.-Experto\n3.-Master")
		nivel = int(input())
		print(modo,nivel)
		if modo == 1 and nivel==1:
			inutil = solo()
		elif modo == 2 and nivel ==1:
			muln = multi_novato()
		elif modo == 1 and nivel==2:
			soloe = solo_experto()
		elif modo==2 and nivel==2:
			multie = multi_experto()
		elif modo == 1 and nivel==3:
			solom = solo_master()
		elif modo == 2 and nivel ==3:
			mulm = multi_master()
		else:
			break	