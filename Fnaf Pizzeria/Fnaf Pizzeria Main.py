import sys
import pygame as pg
#import random
import Animatronics
from manager import StateManager
from states import MainMenu, Gameplay

pg.init()

virtualWidth = 1280
virtualHeight = 720
virtualScreen = pg.Surface((virtualWidth, virtualHeight))

realScreen = pg.display.set_mode((virtualWidth, virtualHeight), pg.FULLSCREEN | pg.SCALED)
realWidth, realHeight = realScreen.get_size()

clock = pg.time.Clock()

all_screens = {
    "MainMenu": MainMenu(),
    "Gameplay": Gameplay()
}

manager = StateManager("MainMenu", all_screens)

"""
def shop():
    for robot in Animatronics.animatronic_list:
        print (robot.name + ": " + str(robot.risk) + ", " + str(robot.entertainment))

shop()
"""

running = True

while running:
    events = pg.event.get()

    for event in events:
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

    dt = clock.tick(60)

    manager.handle_events(events)
    manager.update(dt)

    if manager.state_name == "ExitGame":
        running = False
        continue

    manager.draw(virtualScreen)

    scaledSurface = pg.transform.scale(virtualScreen, (realWidth, realHeight))

    realScreen.blit(scaledSurface, (0, 0))
    pg.display.flip()

"""
    virtualScreen.fill((40, 40, 40))

    pg.draw.circle(virtualScreen, (255, 0, 0), (virtualWidth // 2, virtualHeight // 2), 50)
"""

pg.quit()
sys.exit()