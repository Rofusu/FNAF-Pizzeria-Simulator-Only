import pygame as pg

class Button:
    def __init__(self, x, y, height, width, text="", colour, hoverColour, textColour=(255, 255, 255), image=None):
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.colour = colour
        self.hoverColour = hoverColour
        self.textColour = textColour
        self.font = pg.font.SysFont(None, 30)

        self.image = image
        if self.image is not None:
            self.image = pg.transform.scale(self.image, (width, height))

    def draw(self, surface):
        mousePos = pg.mouse.get_pos()
        isHovered = self.rect.collidepoint(mousePos)

        if self.image is not None:
            surface.blit(self.image, self.rect.topleft)
            if isHovered:
                highlight = pg.surface((self.rect.width, self.rect.height), pg.SRCALPHA)
                highlight.fill((255, 255, 255, 40))
                surface.blit(highlight, self.rect.topleft)

        else:
            currentColour = self.hoverColour if self.rect.collidepoint(mousePos) else self.colour
            pg.draw.rect(surface, currentColour, self.rect)
            pg.draw.rect(surface, (0, 0, 0), self.rect, 2)

            if self.text:
                textSurf = self.font.render(self.text, True, self.textColour)
                textRect = textSurf.get_rect(center=self.rect.center)
                surface.blit(textSurf, textRect)

    def is_clicked(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False