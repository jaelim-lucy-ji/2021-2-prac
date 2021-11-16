# pygame 라이브러리 포함
import math
import pygame

# pygame 초기화
pygame.init()

WIDTH = 800
HEIGHT = 700

# 화면 설정
o_display = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('mini game')

black = (0, 0, 0)
white = (225, 225, 225)
blue = (0, 0, 255)
playerImage = pygame.image.load('D:/abc/player.png')
enemyImage = pygame.image.load('skull.png')


class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('D:/abc/player.png')
        self.dx = 1
        self.dy = 1
        self.rect = self.image.get_bounding_rect()
        self.rect.x = 100
        self.rect.y = 100

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

class enemiee(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('D:/abc/skull.png')
        self.dx = -20
        self.dy = 0
        self.rect = self.image.get_bounding_rect()
        self.rect.x = 0
        self.rect.y = 300
        
    def move(self):
        self.rect.x += self.dx
        if self.rect.x<0:
            self.rect.x=500
            
# 사용자가 중단할 때까지 반복
x = 100
y = 200
dx = 0
dy = 0

# 모든 객체를 하나의 리스트에 저장하여 관리
object_list = pygame.sprite.Group()

player = player()
enemy = enemiee()
object_list.add(enemy, player)
       
running = True
frame_no = 0
while running:
    frame_no += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        player.move(0, -1)
    if key[pygame.K_DOWN]:
        player.move(0, 1)
    if key[pygame.K_RIGHT]:
        player.move(+1, 0)
    if key[pygame.K_LEFT]:
        player.move(-1, 0)
    if (frame_no % 10) == 0:
        enemy.move()

       #흰색 배경
    o_display.fill(white)
    #스프라이트 채우기
    for obj in object_list:
        o_display.blit(obj.image, (obj.rect.x, obj.rect.y))
    
    pygame.display.update()
    
    #충돌 감지
    if pygame.sprite.spritecollideany(player, [enemy]):
        #충돌 감지 후 플레이어 사망 -> 게임 종료
        player.kill()
        print("플레이어 사망!")
        running = False
        
pygame.quit()