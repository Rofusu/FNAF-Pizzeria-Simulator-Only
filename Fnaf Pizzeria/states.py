from ui import Button
import pygame as pg
import ui

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

        self.leftArrowButton = Button(

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

    def handle_events(self, events):
        for event in events:

            if self.menuButton.is_clicked(event):
                self.next_state = "MainMenu"
                self.done = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.next_state = "MainMenu"
                    self.done = True

    def draw(self, screen):
        screen.fill((30, 50, 30))
        text = self.font.render("Playing Game - Press Escape to Quit", True, (255, 255, 255))
        screen.blit(text, (100, 250))

        self.menuButton.draw(screen)