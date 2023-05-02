from pygame import *

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Догонялки / Catch up')

#задай фон сцены
background = transform.scale(image.load('background.png'), (700, 500))

#создай 2 спрайта и размести их на сцене
player1 = transform.scale(image.load('sprite1.png'), (100, 100))
player2 = transform.scale(image.load('sprite2.png'), (100, 100))

#обработай событие «клик по кнопке "Закрыть окно"»
x1, y1 = 10, 10
x2, y2 = 590, 390
speed = 10
clock = time.Clock()
FPS = 120
game = True
while game:
    window.blit(background, (0, 0))
    window.blit(player1, (x1, y1))
    window.blit(player2, (x2, y2))

    keys_pressed = key.get_pressed()

    for e in event.get():
        if e.type == QUIT:
            game = False
        
        if keys_pressed[K_LEFT] and x1 > 5:
            x1 -= speed
        if keys_pressed[K_RIGHT] and x1 < 595:
            x1 += speed
        if keys_pressed[K_UP] and y1 > 5:
            y1 -= speed
        if keys_pressed[K_DOWN] and y1 < 395:
            y1 += speed

        if keys_pressed[K_a] and x2 > 5:
            x2 -= speed
        if keys_pressed[K_d] and x2 < 595:
            x2 += speed
        if keys_pressed[K_w] and y2 > 5:
            y2 -= speed
        if keys_pressed[K_s] and y2 < 395:
            y2 += speed

    clock.tick(FPS)
    display.update()