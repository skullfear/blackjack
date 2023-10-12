import pygame
import random
import sys
from carta import *

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ventana_ancho = 1000
ventana_alto = 700
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Blackjack")

# Tamaño fijo para las imágenes de las cartas
carta_ancho = 100
carta_alto = 150

# Cargar imágenes de cartas
def cargar_cartas(mazo):
    cartas = []
    for carta in mazo:
        valor, pinta, imagen = carta
        imagen = pygame.transform.scale(imagen, (carta_ancho, carta_alto))  # Ajustar tamaño
        cartas.append((valor, pinta, imagen))
    return cartas

def cargar_cartas(mazo):
    cartas = []
    for valor, palo in mazo:
        imagen = pygame.image.load(f'{valor}{palo}.png')
        imagen = pygame.transform.scale(imagen, (carta_ancho, carta_alto))  # Ajustar tamaño
        cartas.append((valor, palo, imagen))
    return cartas


mazo_frances = [(str(x), p) for x in range(2, 11) for p in ['Corazones', 'Diamantes', 'Picas', 'Treboles']] + \
               [('A', p) for p in ['Corazones', 'Diamantes', 'Picas', 'Treboles']] + \
               [('J', p) for p in ['Corazones', 'Diamantes', 'Picas', 'Treboles']] + \
               [('Q', p) for p in ['Corazones', 'Diamantes', 'Picas', 'Treboles']] + \
               [('K', p) for p in ['Corazones', 'Diamantes', 'Picas', 'Treboles']]

mazo_espanol = [(str(x), p) for x in range(2, 8) for p in ['oros', 'copas', 'espadas', 'bastos']] + \
               [('a', p) for p in ['oros', 'copas', 'espadas', 'bastos']] + \
               [('sota', p) for p in ['oros', 'copas', 'espadas', 'bastos']] + \
               [('caballo', p) for p in ['oros', 'copas', 'espadas', 'bastos']] + \
               [('rey', p) for p in ['oros', 'copas', 'espadas', 'bastos']]

# Función para mostrar una carta en la ventana
def mostrar_carta(ventana, carta, x, y):
    ventana.blit(carta[2], (x, y))

# Función para que el jugador elija el mazo
def seleccionar_mazo():
    font = pygame.font.Font(None, 36)
    texto = font.render("Selecciona un mazo:", True, (255, 255, 255))
    texto_rect = texto.get_rect(center=(ventana_ancho // 2, ventana_alto // 2 - 50))

    boton_frances = pygame.Rect(ventana_ancho // 2 - 100, ventana_alto // 2 + 50, 200, 50)
    boton_espanol = pygame.Rect(ventana_ancho // 2 - 100, ventana_alto // 2 + 150, 200, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_frances.collidepoint(event.pos):
                    return mazo_frances
                elif boton_espanol.collidepoint(event.pos):
                    return mazo_espanol

        ventana.fill((0, 128, 0))  # Fondo verde

        pygame.draw.rect(ventana, (0, 0, 255), boton_frances)
        pygame.draw.rect(ventana, (0, 0, 255), boton_espanol)
        ventana.blit(texto, texto_rect)

        font = pygame.font.Font(None, 48)
        texto_frances = font.render("Mazo Francés", True, (255, 255, 255))
        texto_espanol = font.render("Mazo Español", True, (255, 255, 255))
        ventana.blit(texto_frances, (ventana_ancho // 2 - 60, ventana_alto // 2 + 60))
        ventana.blit(texto_espanol, (ventana_ancho // 2 - 65, ventana_alto // 2 + 160))

        pygame.display.update()

# Seleccionar el mazo
mazo_seleccionado = seleccionar_mazo()
cartas = cargar_cartas(mazo_seleccionado)

# Repartir dos cartas a cada jugador
jugador = [random.choice(cartas), random.choice(cartas)]
crupier = [random.choice(cartas), random.choice(cartas)]

# Ciclo principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ventana.fill((0, 128, 0))  # Fondo verde

    # Mostrar cartas de jugador y crupier
    mostrar_carta(ventana, jugador[0], 100, 100)
    mostrar_carta(ventana, jugador[0], 200, 200)
    mostrar_carta(ventana, crupier[1], 300, 300)
    mostrar_carta(ventana, crupier[1], 400, 400)

    pygame.display.update()
