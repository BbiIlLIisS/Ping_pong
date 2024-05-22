from pygame import *

window = display.set_mode((780, 500))

fps = 60
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) #e.g. 55,55 - parameters
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed

        if keys[K_s]:
            self.rect.y += self.speed

    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.speed

        if keys[K_DOWN]:
            self.rect.y += self.speed


FPS = 60
clock = time.Clock()


player1 = Player('Image20240515200819.png', 0, 100, 5, 10, 100)
player2 = Player('Image20240515200819.png', 770, 100, 5, 10, 100)

ball = GameSprite('Image20240515200806.png', 350, 250, 6, 50, 50)

ball_x_speed = 3
ball_y_speed= 3
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.fill((200, 255, 255))            
    player1.reset()
    player1.update_left()
    player2.reset()
    player2.update_right()
    ball.reset()

    if ball_x_speed > 0:
        ball_x_speed = ball_x_speed + 0.001
    else:
        ball_x_speed = ball_x_speed - 0.001

    if ball_y_speed > 0:
         ball_y_speed = ball_y_speed + 0.001
    else:
        ball_y_speed = ball_y_speed - 0.001




    ball.rect.x += ball_x_speed
    ball.rect.y += ball_y_speed

    if ball.rect.y < 0 or ball.rect.y > 450:
        ball_y_speed = ball_y_speed * (-1)
    
    if sprite.collide_rect(ball, player1) or sprite.collide_rect(ball, player2):
        ball_x_speed = ball_x_speed * -1


    clock.tick(fps)
    display.update()