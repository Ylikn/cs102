import pygame
import sys

''' окно '''
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Hello, pygame!')
''' холст '''
screen = pygame.Surface((500, 450))
''' строка состояния '''
status_bar = pygame.Surface((500, 50))


class Sprite:

    def __init__(self, xpos, ypos, filename): # конструктор класса
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((0, 0, 0,))

    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))


def Intersect(x1, y1, x2, y2, r):
    if abs(x1-x2) <= r and abs(y1 - y2) <= r:
        return 1
    else:
        return 0


class Scene: # класс новой сцены

    def __init__(self, punkts=[(200, 90, 'Играть', (250, 250, 30), (250, 30, 250), 0)]): # x,y пункта меню - название пункта - основной цвет - цвет выделенного пункта - номер пункта
        self.punkts = punkts

    def render(self, poverhnost, font, num_punkt): # функци отрисовки пунктов меню (поверхность, шрифт, номер пункта)
        for i in self.punkts:
            if num_punkt == i[5]:
                poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1]-50)) # изменение цвета активного пункта
            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]-50))

    def menu(self):
        done = True
        font_menu = pygame.font.Font(None, 50)
        pygame.key.set_repeat(0, 0) # деактивация залипания клавиш
        pygame.mouse.set_visible(True)# курсор мыши видим
        punkt = 0
        while done:
            status_bar.fill((116, 201, 190))
            screen.fill((116, 201, 190))

            mp = pygame.mouse.get_pos() # блок управления мышью в меню
            for i in self.punkts:
                if i[0] < mp[0] < i[0] + 100 and i[1] < mp[1] < i[1] + 50: # кнопка меню 100 на 50
                    punkt = i[5]
            self.render(screen, font_menu, punkt)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP: # навигацию по меню с помошью клавиш вверх/вниз
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts)-1:
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:# навигацию по меню в помошью мыши
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        sys.exit()
                    elif punkt == 2:
                        done = True
                        self.f1()

            window.blit(status_bar, (0, 0))
            window.blit(screen, (0, 50))
            pygame.display.flip()

    def f1(self):
        done=True
        punkts=[(200, 230, 'Справка', (250, 250, 30), (250, 30, 250), 2)]
        pygame.mouse.set_visible(True) # курсор мыши видим
        punkt = 2
        while done:

            status_bar.fill((116, 201, 190))
            screen.fill((116, 201, 190))

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
            screen.blit(bar_font.render('Мочи пришельца с помощью мыши.', 1, (0, 0, 0)), (10, 10))
            window.blit(status_bar, (0, 0))
            window.blit(screen, (0, 50))
            pygame.display.flip()


''' шрифты '''
pygame.font.init()
speed_font = pygame.font.Font(None, 32)
bar_font = pygame.font.SysFont('Century Gothic', 25 , True, False)
label_font = pygame.font.SysFont(None, 32, True)

''' описание героя '''
hero = Sprite(350, 350, 'hero.png')
''' описание цели '''
zet = Sprite(10, 10, 'hero_2.png')
zet.right = False
zet.step = 1
''' описываем стрелу '''
arrow = Sprite(-40, 350, 'hero_3.png')
arrow.push = False


''' создаём меню '''
punkts = [(200, 90, 'Играть', (250, 250, 30), (250, 30, 250), 0),
          (200, 160, 'Выход', (250, 250, 30), (250, 30, 250), 1),
          (200, 230, 'Справка',(250, 250, 30), (250, 30, 250), 2)]
start = Scene(punkts) # создание экземпляра класса
start.menu() # вызов функции menu для сцены start

''' подготовка к запуску игры '''
done = True
pygame.key.set_repeat(1, 1)
pygame.mouse.set_visible(False)
count = 0 # счет игры
while done:
    ''' обработчик событий '''
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        ''' событие - нажатие клавиш '''
        if e.type == pygame.KEYDOWN:
            ''' перемещение героя '''
            if e.key == pygame.K_LEFT:
                if hero.x > 10:
                    hero.x -= 1
            if e.key == pygame.K_RIGHT:
                if hero.x < 350:
                    hero.x += 1
            if e.key == pygame.K_UP:
                if hero.y > 50:
                    hero.y -= 1
            if e.key == pygame.K_DOWN:
                if hero.y < 350:
                    hero.y += 1
            ''' запуск стрелы '''
            if e.key == pygame.K_SPACE:
                if arrow.push == False:
                    arrow.x = hero.x + 15
                    arrow.y = hero.y
                    arrow.push = True
            if e.key == pygame.K_ESCAPE:
                start.menu()
                pygame.key.set_repeat(1,1) # активация залипания клавиш
                pygame.mouse.set_visible(False) # курсор мыши невидим
        ''' событие - движение мыши '''
        if e.type == pygame.MOUSEMOTION:
            pygame.mouse.set_visible(False)
            m = pygame.mouse.get_pos()
            if  10 < m[0] < 350:
                hero.x = m[0]
            if 50 < m[1] < 350:
                hero.y = m[1]
        ''' событие - нажатие кнопок мыши '''
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                if arrow.push == False:
                    arrow.x = hero.x+15
                    arrow.y = hero.y
                    arrow.push = True

    ''' заливка '''
    screen.fill((0, 132, 114))
    status_bar.fill((153, 220, 217))
    ''' передвижение цели '''
    if zet.right == True:
        zet.x -= zet.step
        if zet.x < 0:
            zet.right = False
    else:
        zet.x += zet.step
        if zet.x > 350:
            zet.right = True
    ''' перемещение стрелы '''
    if arrow.y < 0:
        arrow.push = False
        count -= 1
    if not arrow.push:
        arrow.y = 350
        arrow.x = -40
    else:
        arrow.y -= 1
    ''' столкновение стрелы и цели '''
    if Intersect(arrow.x + 10, arrow.y + 20, zet.x + 20, zet.y + 20, 10):
        arrow.push = False
        zet.step += 0.2
        count  += 1
    ''' отрисовка объектов '''
    arrow.render()
    zet.render()
    hero.render()
    ''' отрисовка шрифтов '''
    status_bar.blit(bar_font.render('Счет: ' + str(count), 1, (0, 0, 0)), (10, 10))
    status_bar.blit(bar_font.render('Скорость: ' + str(zet.step), 1, (0, 0, 0)), (320, 10))
    ''' отображение холста на экран '''
    window.blit(screen, (0, 50))
    window.blit(status_bar, (0, 0))
    pygame.display.flip()
    pygame.time.delay(5)
