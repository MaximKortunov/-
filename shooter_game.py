#Создай собственный Шутер!

from pygame import *
from random import *
font.init()
win_width=700
win_height=500
window = display.set_mode((win_width,win_height))
display.set_caption("Шутер")
speed = 10
lost=0
life=3
score = 0
score1 = 0
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y    
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y<0:
            self.kill()
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet=Bullet("bullet.png",self.rect.centerx,self.rect.top,15,20,5)
        bullets.add(bullet)

        
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y>=win_height:
            self.rect.x=randint(80,win_width-80)
            self.rect.y=0
            lost = lost + 1


background = transform.scale(image.load("galaxy.jpg"),(win_width,win_height))
clock=time.Clock()
FPS=60
hero = Player("rocket.png",5,win_height-130,30,30,4)
bullet=Bullet("bullet.png",5,win_height-130,30,30,4)
monsters=sprite.Group()
bullets=sprite.Group()

for i in range(1,6):
    monstr=Enemy("ufo.png",randint(1,700),-40,80,50,randint(1,5))
    monsters.add(monstr)
font1 = font.Font(None,40)
win=font1.render("Победа",True,(255, 255, 224))





mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                hero.fire()
    if sprite.spritecollide(hero,monsters,False):
        game = False
    a= sprite.groupcollide(bullets,monsters,True, True)

    for i in a:
        score += 1
        monsters.add(monstr)
    if  sprite.groupcollide(bullets,monsters,True, True):
        score1 += 1
  
    if score1 == 1:
        game = False

    
            
    
       
    window.blit(background,(0,0))
    hero.update()
    hero.reset()

    bullets.update()
    bullets.draw(window)
    monsters.draw(window)
    monsters.update()
    display.update()
    clock.tick(FPS)