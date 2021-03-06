import time
import pygame
from bottle import Bottle, route, run, template


app = Bottle()
pygame.init()



@app.get('/')
def index():
	return template('index')

@app.post('/roar')
def roar():
    pygame.mixer.music.load('roar.wav')
    pygame.mixer.music.play()
    time.sleep(10)

@app.post('/stego')
def roar():
    pygame.mixer.music.load('stegosaurus.wav')
    pygame.mixer.music.play()
    time.sleep(10)

run(app, host='localhost', port=8080)	