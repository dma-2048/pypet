import pygame
from pygame.freetype import Font, init
from json import load

init()
comic_sans = Font("fonts/comic_sans.ttf", 15)
papyrus = Font("fonts/papyrus.ttf", 15)
determination_mono = Font("fonts/determination_mono.otf", 40/3)
determination_sans = Font("fonts/determination_sans.otf", 40/3)
file = open("stats.json")
stats = load(file)
file.close()
wellness = stats["wellness"]
items = stats["items"]

def toggle_wellness_sidebar(sidebar):
	if sidebar.hidden:
		sidebar.hidden = False
		for i, attribute in enumerate(wellness.keys()):
			sidebar.add(Text(sidebar.window, sidebar.rect.x + 5, sidebar.rect.y + 5 + (i * 35), determination_sans, f"{attribute}:", (255, 255, 255), (0, 0, 0)))
			sidebar.add(Text(sidebar.window, sidebar.rect.x + 5, sidebar.rect.y + 23 + (i * 35), determination_sans, str(wellness[attribute]), (255, 255, 255), (0, 0, 0)))
			sidebar.add(ProgressBar(sidebar.window, sidebar.rect.x + 30, sidebar.rect.y + 22 + (i * 35), 80, 12, (0, 0, 255)))
	else:
		sidebar.hidden = True
		sidebar.clear()

def toggle_items_sidebar(sidebar):
	if sidebar.hidden:
		sidebar.hidden = False
		for i, item in enumerate(items):
			sidebar.add(Text(sidebar.window, sidebar.rect.x + 5, sidebar.rect.y + 5 + (i * 20), determination_sans, f"- {item}", (255, 255, 255), (0, 0, 0)))
	else:
		sidebar.hidden = True
		sidebar.clear()

class Text:
	def __init__(self, window: pygame.Surface, x: int, y: int, font: Font, text: str, color: tuple, background: tuple = None):
		self.window = window
		self.rect = pygame.Rect(x, y, 0, 0)
		self.font = font
		self.color = color
		self.background = background
		self.text = font.render(text, color, background)[0]

	def move(self, x: int, y: int):
		self.rect.x, self.rect.y = x, y

	def draw(self):
		self.window.blit(self.text, (self.rect.x, self.rect.y))

	def edit(self, text: str):
		self.text = self.font.render(text, self.color, self.background)[0]

class ProgressBar:
	def __init__(self, window: pygame.Surface, x: int, y: int, width: int, height: int, color: tuple):
		self.window = window
		self.border = pygame.Rect(x - 1, y - 1, width + 2, height + 2)
		self.rect = pygame.Rect(x, y, width, height)
		self.color = color

	def move(self, x: int, y: int):
		self.border.x, self.border.y = x - 1, y - 1
		self.rect.x, self.rect.y = x, y

	def draw(self):
		pygame.draw.rect(self.window, (255, 255, 255), self.border)
		pygame.draw.rect(self.window, self.color, self.rect)