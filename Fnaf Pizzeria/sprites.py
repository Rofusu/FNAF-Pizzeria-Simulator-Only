import pygame as pg

images = {}
load = pg.image.load

def load_all_assets():
    #try:
    images["r_arrow"] = load("Random Games/Fnaf Pizzeria/assets/r_arrow.png").convert_alpha()
    images["l_arrow"] = load("Random Games/Fnaf Pizzeria/assets/l_arrow.png").convert_alpha()
    images["Freddy"] = load("Random Games/Fnaf Pizzeria/assets/Bear5.png").convert_alpha()
    #except pg.error as error:
        #print (f"Error loading assets: {error}")
        