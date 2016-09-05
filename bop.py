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
def solo():

	ins = ["Gira","Golpea","Jala"]
	pygame.init()
	ventana = pygame.display.set_mode((800,600))
	pygame.display.set_caption("Bop it")
	reloj = pygame.time.Clock()
	correcto = True
	inicio = time.time()
	chido=0
	while time.time()-inicio< 3 and correcto==True:
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
		print("Felicidades Nivel desbloqueado")
	else:
		display_mensaje("Ya valiste",ventana)
		ventana.fill((0,0,0))
	pygame.display.quit()
	pygame.quit()
	return chido





print("Bienvenido al excitante juego BOP IT!!\nSelecciona modo de juego:")
print("1.- Solo")
print("2.- Multijugador")
modo = int(input())
if modo==1:
	chido = solo()
else:
	print("Aun no programado ==========")
print(chido)
if chido>=3:
	print("Bienvenido al excitante juego BOP IT!!\nSelecciona modo de juego:")
	print("1.- Solo")
	print("2.- Multijugador")
	modo = int(input())
	print("Nivel de dificultad:\n1.-Novato\n2.-Experto")
	nivel = int(input())
	if modo == 1 and nivel==1:
		inutil = solo()
	if modo == 2 and nivel ==1:
		print(hola)
