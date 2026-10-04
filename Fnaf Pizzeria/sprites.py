import pygame as pg

images = {}
load = pg.image.load

def load_all_assets():
    #try:
    images["r_arrow"] = load("Fnaf Pizzeria/assets/r_arrow.png").convert_alpha()
    images["l_arrow"] = load("Fnaf Pizzeria/assets/l_arrow.png").convert_alpha()
    images["Freddy"] = load("Fnaf Pizzeria/assets/Bear5.png").convert_alpha()
    images["Chica"] = load("Fnaf Pizzeria/assets/red_chica.png").convert_alpha()
    images["Bonnie"] = load("Fnaf Pizzeria/assets/bonnie.png").convert_alpha()
    images["Toy Chica"] = load("Fnaf Pizzeria/assets/toy_chica.png").convert_alpha()
    images["Raggy"] = load("Fnaf Pizzeria/assets/rag.png").convert_alpha()
    images["Mr Toaster"] = load("Fnaf Pizzeria/assets/toaster.png").convert_alpha()
    #except pg.error as error:
        #print (f"Error loading assets: {error}")
        