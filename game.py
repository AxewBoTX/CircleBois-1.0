import pygame,os,time,random
from Data.player import*
from Data.button import*
from Data.ball import*

class Game():
	def __init__(self):
		#Main Window
		pygame.init()
		self.main_width = 1000
		self.main_height = 700
		self.window = pygame.display.set_mode((
			self.main_width,self.main_height))
		pygame.display.set_caption("Window")
		self.window_icon = pygame.image.load("icon.ico")
		pygame.display.set_icon(self.window_icon)
		self.myfont = pygame.font.Font(
			os.path.join("Assets","main_font.ttf"),100)
		self.score_font = pygame.font.Font(
			os.path.join("Assets","score_font.ttf"),40)

		#Game State Control Strcuture
		self.running = True
		self.starting = True
		self.playing = False
		self.won = False
		self.lost =  False

		#Game Assets
		self.FPS = 240
		self.last_time = time.time()
		self.main_clock = pygame.time.Clock()

		#Buttons
		start_button_image = pygame.image.load(
			os.path.join("Assets","start_button.png"))
		self.start_button = Button(500,350,start_button_image)
		starting_exit_button_image = pygame.image.load(
			os.path.join("Assets","exit_button.png"))
		self.starting_exit_button = Button(500,550,starting_exit_button_image)
		about_button_image = pygame.image.load(
			os.path.join("Assets","about_button.png"))
		self.about_button = Button(880,670,about_button_image)
		intro_button_image = pygame.image.load(
			os.path.join("Assets","intro_button.png"))
		self.intro_button = Button(120,670,intro_button_image)

		#Text
		self.circle_text = self.myfont.render(
			"CIRCLE",False,'black')
		self.bois_text = self.myfont.render(
			"BOIS",False,'black')
		self.lost_text = self.myfont.render(
			"LOST",False,'black')
		self.game_exit_text = self.myfont.render(
			"JUST EXIT THE GAME",False,'black')
		self.you_won_text = self.myfont.render(
			"YOU WON",False,'black')
		self.congratulations = self.myfont.render(
			"CONGRATULATION",False,'black')

		#Player
		player_x = random.randint(100,900)
		player_y = random.randint(100,600)
		self.player = Player(player_x,player_y,self.score_font)
		self.player_vel = 2.5
		#Good Ball
		green_ball_x = random.randint(100,900)
		green_ball_y = random.randint(100,600)
		green_ball_r = random.randint(20,30)
		self.green_ball = Ball(green_ball_x,green_ball_y,green_ball_r,self.window,'green')
		#Bad Ball
		red_ball_x = random.randint(100,900)
		red_ball_y = random.randint(100,600)
		red_ball_r = random.randint(30,40)
		self.red_ball = Ball(red_ball_x,red_ball_y,red_ball_r,self.window,'red')

		#Window Borders
		self.left_window_border = pygame.Rect(
			0,0,10,700)
		self.right_window_border = pygame.Rect(
			990,0,10,700)
		self.top_window_border = pygame.Rect(
			0,0,1000,10)
		self.bottom_window_border = pygame.Rect(
			0,690,1000,10)

	#Starting Window
	def starting_window(self):
		#Delta Time
		dt = time.time() - self.last_time
		dt *= 240
		self.last_time = time.time()

		#Window Structure
		self.window.fill('white')
		#Text Blitting
		self.window.blit(self.circle_text,(380,50))
		self.window.blit(self.bois_text,(420,150))
		#Button Blitting
		#Start Button
		if self.start_button.draw_button(self.window):
			self.starting = False
			self.playing = True
			self.won = False
			self.lost = False
		#Exit Button
		if self.starting_exit_button.draw_button(self.window):
			self.running = False
		#About Button
		if self.about_button.draw_button(self.window):
			os.system("Data\\About.txt")
		#Intro Button
		if self.intro_button.draw_button(self.window):
			os.system("INTRO.txt")

		#Events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
		pygame.display.update()
		self.main_clock.tick(self.FPS)

	#Game Window
	def game_window(self):
		#Delta Time
		dt = time.time() - self.last_time
		dt *= 240
		self.last_time = time.time()

		#Window Structure
		self.window.fill('white')
		self.player.draw_player(self.window)
		self.green_ball.draw()
		self.green_ball.move(dt)
		self.red_ball.draw()
		self.red_ball.move(dt)
		self.player.check_green_contact(self.green_ball)
		self.player.check_red_contact(self.red_ball)
		self.window.blit(self.player.score_var,(10,5))

		#WON OR LOST
		#WON
		if self.player.score >= 500:
			self.starting = False
			self.playing = False
			self.won = True 
			self.lost = False
		#LOST
		if self.player.score <= 0:
			self.starting = False
			self.playing = False
			self.won = False
			self.lost = True
		
		#Window Borders
		pygame.draw.rect(self.window,'black',self.top_window_border)
		pygame.draw.rect(self.window,'black',self.bottom_window_border)
		pygame.draw.rect(self.window,'black',self.right_window_border)
		pygame.draw.rect(self.window,'black',self.left_window_border)	
		#Player Movement
		key_pressed = pygame.key.get_pressed()
		#LEFT
		if key_pressed[pygame.K_a]:
			if self.player.x - self.player_vel > 0:
				self.player.x -= self.player_vel*dt
		#RIGHT
		if key_pressed[pygame.K_d]:
			if self.player.x + self.player_vel < 900:
				self.player.x += self.player_vel*dt
		#TOP
		if key_pressed[pygame.K_w]:
			if self.player.y - self.player_vel > 0:
				self.player.y -= self.player_vel*dt
		#BOTTOM
		if key_pressed[pygame.K_s]:
			if self.player.y + self.player_vel < 600:
				self.player.y += self.player_vel*dt

		#Events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

		pygame.display.update()
		self.main_clock.tick(self.FPS)	

	#Won Window
	def won_window(self):
		#Delta Time
		dt = time.time() - self.last_time
		dt *= 240
		self.last_time = time.time()

		#Window Structure
		self.window.fill('white')
		self.window.blit(self.you_won_text,(330,50))
		self.window.blit(self.congratulations,(180,250))
		if self.starting_exit_button.draw_button(self.window):
			self.running = False

		#Events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
		pygame.display.update()
		self.main_clock.tick(self.FPS)

	#Lost Window
	def lost_window(self):
		#Delta Time
		dt = time.time() - self.last_time
		dt *= 240
		self.last_time = time.time()

		#Window Structure
		self.window.fill('white')
		self.window.blit(self.lost_text,(420,50))
		self.window.blit(self.game_exit_text,(100,250))
		if self.starting_exit_button.draw_button(self.window):
			self.running = False

		#Events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
		pygame.display.flip()
		self.main_clock.tick(self.FPS)