import random
import pygame

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./meteor.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./player.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = 0

    def changespeed(self, x):
        self.speed_x += x

    def update(self):
        self.rect.x += self.speed_x
        player.rect.y = 510

class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./laser.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 5

def mostrar_puntuacon():
    fuente = pygame.font.SysFont('Consolas', 30)
    texto = fuente.render(str(score).zfill(5), True, (WHITE))
    texto_rect = texto.get_rect()
    texto_rect.topleft = [0, 0]
    screen.blit(texto, texto_rect)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
pygame.init()

screen = pygame.display.set_mode([900, 600])
clock = pygame.time.Clock()
done = False
score = 0

all_sprite_list = pygame.sprite.Group()
meteor_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()

for i in range(50):
    meteor = Meteor()
    meteor.rect.x = random.randrange(880)
    meteor.rect.y = random.randrange(450)

    meteor_list.add(meteor)
    all_sprite_list.add(meteor)

player = Player()
all_sprite_list.add(player)
sound = pygame.mixer.Sound("./laser5.ogg")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3)
            if event.key == pygame.K_RIGHT:
                player.changespeed(3)
            if event.key == pygame.K_SPACE:
                laser = Laser()
                laser.rect.x = player.rect.x + 45
                laser.rect.y = player.rect.y - 20

                all_sprite_list.add(laser)
                laser_list.add(laser)
                sound.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3)
            if event.key == pygame.K_RIGHT:
                player.changespeed(-3)
            
    all_sprite_list.update()

    for laser in laser_list:
        meteor_hit_list = pygame.sprite.spritecollide(laser, meteor_list, True)
        for meteor in meteor_hit_list:
            all_sprite_list.remove(laser)
            laser_list.remove(laser)
            score += 10
            print(score)
        if laser.rect.y < -10:
            all_sprite_list.remove(laser)
            laser_list.remove(laser)

    screen.fill(BLACK)
    all_sprite_list.draw(screen)

    mostrar_puntuacon()

    pygame.display.flip()
    clock.tick(60)