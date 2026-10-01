from ui import Button
import pygame as pg
from sprites import images
#import ui


class BaseState:
    def __init__(self):
        self.next_state = None
        self.done = False

    def handle_events(self, events):
        pass
    def update(self, dt):
        pass
    def draw(self, screen):
        pass


class MainMenu(BaseState):
    def __init__(self):
        super().__init__()
        self.font = pg.font.SysFont(None, 40)

        self.startButton = Button(
            x = 540, y=300, width=200, height=50,
            text="Start", colour=(50, 150, 50), hoverColour=(70, 180, 70)
        )

        self.quitButton = Button(
            x=540, y=370, width=200, height=50,
            text="Quit", colour=(255, 0, 0), hoverColour=(150, 0, 0)
        )

    def handle_events(self, events):
        for event in events:

            if self.startButton.is_clicked(event):
                self.next_state = "Gameplay"
                self.done = True

            if self.quitButton.is_clicked(event):
                self.next_state = "ExitGame"
                self.done = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.next_state = "Gameplay"
                    self.done = True

    def draw(self, screen):
        screen.fill((30, 30, 50))
        text = self.font.render("Main Menu: Press Enter to Start", True, (255, 255, 255))
        screen.blit(text, (100, 250))

        self.startButton.draw(screen)
        self.quitButton.draw(screen)


class Gameplay(BaseState):
    def __init__(self):
        super().__init__()
        self.font = pg.font.SysFont(None, 40)

        self.menuButton = Button(
            x=20, y=20, width=150, height=80,
            text="Menu", colour=(100, 100, 100), hoverColour=(150, 150, 150)
        )
        self.shopButton = Button(
            x=20, y=100, width=150, height=80,
            text="Shop", colour=(100, 100, 100), hoverColour=(150, 150, 150)
        )

    def handle_events(self, events):
        for event in events:

            if self.menuButton.is_clicked(event):
                self.next_state = "MainMenu"
                self.done = True

            if self.shopButton.is_clicked(event):
                self.next_state = "Shop"
                self.done = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.next_state = "MainMenu"
                    self.done = True

    def draw(self, screen):
        screen.fill((30, 50, 30))
        text = self.font.render("Playing Game", True, (255, 255, 255))
        screen.blit(text, (100, 250))

        self.menuButton.draw(screen)
        self.shopButton.draw(screen)

class Shop(BaseState):
    def __init__(self):
        super().__init__()
        self.font = pg.font.SysFont(None, 40)

        self.lArrowButton = Button(
            x=200, y=600, height=100, width=100, colour=None, hoverColour=None, image=images["l_arrow"]
        )
        self.rArrowButton = Button(
            x=800, y=600, height=100, width=100, colour=None, hoverColour=None, image=images["r_arrow"]
        )

    def handle_events(self, events):
        for event in events:

            if self.lArrowButton.is_clicked(event):
                self.next_state = "Gameplay"
                self.done = True

            if self.rArrowButton.is_clicked(event):
                self.next_state = "Gameplay"
                self.done = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.next_state = "Gameplay"
                    self.done = True

    def draw(self, screen):
        screen.fill((100, 200, 200))
        text = self.font.render("Shop", True, (255, 255, 255))
        screen.blit(text, (100, 250))

        self.lArrowButton.draw(screen)
        self.rArrowButton.draw(screen)