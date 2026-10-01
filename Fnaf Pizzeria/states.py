from ui import Button
import pygame as pg
from sprites import images
from animatronics import animatronic_dict, animatronic_order, playerCash
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
        self.fontBig = pg.font.SysFont(None, 60)
        self.fontMedium = pg.font.SysFont(None, 40)
        self.fontSmall = pg.font.SysFont(None, 20)

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
        text = self.fontSmall.render("Main Menu: Press Enter to Start", True, (255, 255, 255))
        screen.blit(text, (100, 250))

        self.startButton.draw(screen)
        self.quitButton.draw(screen)


class Gameplay(BaseState):
    def __init__(self):
        super().__init__()
        self.fontBig = pg.font.SysFont(None, 60)
        self.fontMedium = pg.font.SysFont(None, 40)
        self.fontSmall = pg.font.SysFont(None, 20)

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
        text = self.fontSmall.render("Playing Game", True, (255, 255, 255))
        screen.blit(text, (100, 250))

        self.menuButton.draw(screen)
        self.shopButton.draw(screen)

class Shop(BaseState):
    def __init__(self):
        super().__init__()
        self.fontBig = pg.font.SysFont(None, 60)
        self.fontMedium = pg.font.SysFont(None, 40)
        self.fontSmall = pg.font.SysFont(None, 20)

        self.currentIndex = 0
        self.currentAnimatronic = animatronic_dict[animatronic_order[self.currentIndex]]


        self.lArrowButton = Button(
            x=500, y=525, height=100, width=100,
            colour=None, hoverColour=None, image=images["l_arrow"]
        )
        self.rArrowButton = Button(
            x=1080, y=525, height=100, width=100,
            colour=None, hoverColour=None, image=images["r_arrow"]
        )

        self.backButton = Button(
            x=20, y=20, height=50, width=150, text="Back",
            colour=(100, 100, 100), hoverColour=(150, 150, 150)
        )

        self.buyButton = Button(
            x=50, y=600, height=60, width=320, text="Buy",
            colour=(50, 150, 50), hoverColour=(70, 180, 70)
        )

    def cycle_animatronic(self, direction):
        #direction is 1 for right, and -1 for left btw
        self.currentIndex = (self.currentIndex + direction) % len(animatronic_order)
        self.currentAnimatronic = animatronic_dict[animatronic_order[self.currentIndex]]

    def handle_events(self, events):
        for event in events:

            if self.lArrowButton.is_clicked(event):
                self.cycle_animatronic(-1)

            if self.rArrowButton.is_clicked(event):
                self.cycle_animatronic(1)

            if self.backButton.is_clicked(event):
                self.next_state = "Gameplay"
                self.done = True

            if self.buyButton.is_clicked(event):
                self.purchase_animatronic()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.next_state = "Gameplay"
                    self.done = True

    def purchase_animatronic(self):
        global playerCash
        if self.currentAnimatronic.owned:
            #make sure they cant purchase it
            pass
        elif playerCash >= self.currentAnimatronic.cost:
            playerCash -= self.currentAnimatronic.cost
            self.currentAnimatronic.owned = True


    def draw_stats(self, screen):
        boxWidth = 300
        boxHeight = 200
        boxX = 50
        boxY = 150

        pg.draw.rect(screen, (50, 50, 50), (boxX, boxY, boxWidth, boxHeight))
        pg.draw.rect(screen, (200, 200, 200), (boxX, boxY, boxWidth, boxHeight), 2)

        yOffset = boxY + 15

        name_surf = self.fontBig.render(self.currentAnimatronic.name, True, (255, 255, 100))
        screen.blit(name_surf, (boxX + 15, boxY - 50))
        yOffset += 45

        risk_text = f"Risk: {self.currentAnimatronic.risk}/10"
        risk_surf = self.fontMedium.render(risk_text, True, (255, 100, 100))
        screen.blit(risk_surf, (boxX + 15, yOffset))
        yOffset += 35

        # Entertainment rating
        ent_text = f"Entertainment: {self.currentAnimatronic.entertainment}/10"
        ent_surf = self.fontMedium.render(ent_text, True, (100, 255, 100))
        screen.blit(ent_surf, (boxX + 15, yOffset))
        yOffset += 35

        # Cost
        cost_text = f"Cost: ${self.currentAnimatronic.cost}"
        cost_surf = self.fontMedium.render(cost_text, True, (100, 200, 255))
        screen.blit(cost_surf, (boxX + 15, yOffset))

    def draw(self, screen):
        screen.fill((0, 100, 150))

        # Animatronic name in center
        #center_name = self.fontBig.render(self.currentAnimatronic.name, True, (255, 255, 100))
        #screen.blit(center_name, (640 - center_name.get_width() // 2, 250))

        # Description
        desc = self.fontMedium.render(self.currentAnimatronic.description, True, (200, 200, 200))
        screen.blit(desc, (desc.get_width() // 2, 425))

        cash = self.fontBig.render(f"$ {str(playerCash)}", True, (0, 150, 25))
        screen.blit(cash, (1100 - cash.get_width() // 2, 100))

        # Status (owned or not)
        if self.currentAnimatronic.owned:
            status_text = "Owned"
            status_colour = (100, 255, 100)
        else:
            status_text = "Not Owned"
            status_colour = (255, 100, 100)

        status_surf = self.fontBig.render(status_text, True, status_colour)
        screen.blit(status_surf, ((status_surf.get_width() // 2) - 15, 360))

        # Draw stats box in corner
        self.draw_stats(screen)

        if not self.currentAnimatronic.image == None:
            screen.blit(self.currentAnimatronic.image, (680, 75))

        # Draw buttons
        self.backButton.draw(screen)
        self.lArrowButton.draw(screen)
        self.rArrowButton.draw(screen)
        self.buyButton.draw(screen)