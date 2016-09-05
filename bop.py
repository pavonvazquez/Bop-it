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
	while time.time()-inicio< 3:
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
	while time.time()-inicio< 3:
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
	while time.time()-inicio< 1:
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

def fiesta_novato():

	ins = ["Gira","Golpea","Jala","Pasala"]
	pygame.init()
	ventana = pygame.display.set_mode((800,600))
	pygame.display.set_caption("Bop it")
	reloj = pygame.time.Clock()
	correcto = True
	inicio = time.time()
	chido=0
	while time.time()-inicio< 3:
		time.sleep(3)
		i = randint(0,3)
		display_mensaje(ins[i],ventana)
		ventana.fill((0,0,0))
		if(i==2):
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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
				if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
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

def fiesta_experto():
	ins = ["Gira","Golpea","Jala","Pasala","1","2","3"]
	pygame.init()
	ventana = pygame.display.set_mode((800,600))
	pygame.display.set_caption("Bop it")
	reloj = pygame.time.Clock()
	correcto = True
	inicio = time.time()
	chido=0
	while time.time()-inicio< 3:
		time.sleep(2)
		i = randint(0,6)
		display_mensaje(ins[i],ventana)
		ventana.fill((0,0,0))
		if(i==2):
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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
				if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
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
				if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
					display_mensaje("Correcto",ventana)
					ventana.fill((0,0,0))
					correcto = True
					inicio = time.time()
					chido+=1
		if(i==6):
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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
def fiesta_master():
	ins = ["Gira","Golpea","Jala","1","2","3","Pasala",(255,255,0),(255,255,255),(0,0,255)]
	pygame.init()
	ventana = pygame.display.set_mode((800,600))
	pygame.display.set_caption("Bop it")
	reloj = pygame.time.Clock()
	correcto = True
	inicio = time.time()
	chido=0
	while time.time()-inicio< 1:
		time.sleep(1)
		i = randint(0,9)
		if 0<=i<=6:
			display_mensaje(ins[i],ventana)
			ventana.fill((0,0,0))
			if(i==2):
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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
					if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
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
					if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
						display_mensaje("Correcto",ventana)
						ventana.fill((0,0,0))
						correcto = True
						inicio = time.time()
						chido+=1
			if(i==5):
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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
					if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
						display_mensaje("Correcto",ventana)
						ventana.fill((0,0,0))
						correcto = True
						inicio = time.time()
						chido+=1
			if(i==9):
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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
chido = 0
muln = 0
fn = 0
fe = 0
fm = 0
soloe=0
mule=0
solom = 0
mulm = 0
lista_m_n = []
lista_f_n = []
print("Bienvenido al excitante juego BOP IT!!\nSelecciona modo de juego:")
print("\n\nLas instrucciones son las siguientes:n\n\nHay tres modos de juego:")
print("Solo, habra las siguientes  instrucciones, golpea (barra espaciadora), gira (scroll), jala (click derecho)")
print("1 (equivalente a gira), 2 (equivalente a golpea), 3 (equivalente a jala)")
print("pantalla amarilla (equivalente a gira), pantalla blanca (equivalente a golpea), pantalla azul (equivalente a jala) ")
print("\n\nMultijugador, habra multiples jugadores donde la isntruccion adherida es pasala (flecha a la derecha), el ganador sera aquel que logre mas puntos")
print("\n\nFiesta parecido a multijugador, donde las instrucciones que cambian son golpea (flecha abajo), jala(click izquierdo)")
print("2 (equivalente a golpea), 3 (equivalente a jala), pantalla blanca (equivalente a golpea) y pantalla  azul (equivalente a jala)")
print("\n\n La unica forma de desbloquear todos los niveles es a traves del modo solo:\n\nA jugar y exito!!!!\n\n\n")
print("1.- Solo")
print("2.- Multijugador")
print("3.- Fiesta")
modo = int(input())
if modo==1:
	chido = solo()
elif modo==2:
	n = int(input("Numero de jugadores:  "))
	for i in range(n):
		print("Adelante jugador "+str(i+1))
		muln = multi_novato()
		lista_m_n.append(muln)
	print("El ganador fue ",lista_m_n.index(max(lista_m_n))+1," con ",max(lista_m_n))
else:
	n = int(input("Numero de jugadores:  "))
	for i in range(n):
		print("Adelante jugador "+str(i+1))
		fn = fiesta_novato()
		lista_f_n.append(fn)
	print("El ganador fue ",lista_f_n.index(max(lista_f_n))+1," con ",max(lista_f_n))

lista_m_n = []
lista_f_n = []
if chido>=3:
	print("Felicidades Nivel Desblqueado")
	while modo!=4 or soloe<3: 
		lista_m_n = []
		lista_f_n = []
		print("Bienvenido al excitante juego BOP IT!!\nSelecciona modo de juego:")
		print("1.- Solo")
		print("2.- Multijugador")
		print("3.- Fiesta")
		print("4.- Salir :c")
		modo = int(input())
		print("Nivel de dificultad:\n1.-Novato\n2.-Experto")
		nivel = int(input())
		print(modo,nivel)
		if modo == 1 and nivel==1:
			inutil = solo()
		elif modo == 2 and nivel ==1:
			n = int(input("Numero de jugadores:  "))
			for i in range(n):
				print("Adelante jugador "+str(i+1))
				muln = multi_novato()
				lista_m_n.append(muln)
			print("El ganador fue ",lista_m_n.index(max(lista_m_n))+1," con ",max(lista_m_n))
		elif modo == 1 and nivel==2:
			soloe = solo_experto()
		elif modo==2 and nivel==2:
			n = int(input("Numero de jugadores:  "))
			for i in range(n):
				print("Adelante jugador "+str(i+1))
				muln = multi_experto()
				lista_m_n.append(muln)
			print("El ganador fue ",lista_m_n.index(max(lista_m_n))+1," con ",max(lista_m_n))
		elif modo == 3 and nivel==1:
			n = int(input("Numero de jugadores:  "))
			for i in range(n):
				print("Adelante jugador "+str(i+1))
				fe = fiesta_experto()
				lista_f_n.append(fe)
			print("El ganador fue ",lista_f_n.index(max(lista_f_n))+1," con ",max(lista_f_n))
		elif modo == 3 and nivel==2:
			for i in range(n):
				print("Adelante jugador "+str(i+1))
				fe = fiesta_experto()
				lista_f_n.append(fe)
			print("El ganador fue ",lista_f_n.index(max(lista_f_n))+1," con ",max(lista_f_n))
		else:
			break
		if(modo==4 or soloe>=3):
			break
lista_m_n = []
lista_f_n = []
if soloe>=3:
	print("Felicidades has desbloqueado todos los niveles!!!!")
	while modo!=3:
		lista_m_n = []
		lista_f_n = []
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
			n = int(input("Numero de jugadores:  "))
			for i in range(n):
				print("Adelante jugador "+str(i+1))
				muln = multi_novato()
				lista_m_n.append(muln)
			print("El ganador fue ",lista_m_n.index(max(lista_m_n))+1," con ",max(lista_m_n))
		elif modo == 1 and nivel==2:
			soloe = solo_experto()
		elif modo==2 and nivel==2:
			n = int(input("Numero de jugadores:  "))
			for i in range(n):
				print("Adelante jugador "+str(i+1))
				muln = multi_experto()
				lista_m_n.append(muln)
			print("El ganador fue ",lista_m_n.index(max(lista_m_n))+1," con ",max(lista_m_n))
		elif modo == 1 and nivel==3:
			solom = solo_master()
		elif modo==2 and nivel==2:
			n = int(input("Numero de jugadores:  "))
			for i in range(n):
				print("Adelante jugador "+str(i+1))
				muln = multi_master()
				lista_m_n.append(muln)
			print("El ganador fue ",lista_m_n.index(max(lista_m_n))+1," con ",max(lista_m_n))
		elif modo == 3 and nivel==1:
			n = int(input("Numero de jugadores:  "))
			for i in range(n):
				print("Adelante jugador "+str(i+1))
				fe = fiesta_experto()
				lista_f_n.append(fe)
			print("El ganador fue ",lista_f_n.index(max(lista_f_n))+1," con ",max(lista_f_n))
		elif modo == 3 and nivel==2:
			for i in range(n):
				print("Adelante jugador "+str(i+1))
				fe = fiesta_experto()
				lista_f_n.append(fe)
			print("El ganador fue ",lista_f_n.index(max(lista_f_n))+1," con ",max(lista_f_n))
		elif modo == 3 and nivel==3:
			for i in range(n):
				print("Adelante jugador "+str(i+1))
				fe = fiesta_master()
				lista_f_n.append(fe)
			print("El ganador fue ",lista_f_n.index(max(lista_f_n))+1," con ",max(lista_f_n))
		else:
			break	