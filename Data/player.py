import pygame,os,time,math

class Player():
	def __init__(self,x,y,font):
		self.x = x
		self.y = y
		self.font = font
		self.player_width = 100
		self.player_height = 100
		self.player_image = pygame.image.load(
			os.path.join("Assets","circle_boi.png"))
		self.player = pygame.transform.rotate(
			pygame.transform.scale(
				self.player_image,(self.player_width,self.player_height)),0)
		self.player_rect = pygame.Rect(self.x,self.y,self.player_width,self.player_height)
		self.touching_green_ball = False
		self.touching_red_ball = False
		self.score = 50
	def draw_player(self,master):
		master.blit(self.player,(self.x,self.y))
	def check_green_contact(self,ball):
		if math.sqrt((self.y - ball.y) ** 2 + (self.x - ball.x) ** 2) < self.player_width/2 + ball.r:
			if self.touching_green_ball == False:
				self.score += 10
				self.touching_green_ball = True
		else:
			self.touching_green_ball = False
		self.score_var = self.font.render("SCORE:"+str(self.score),False,'black')
	def check_red_contact(self,ball):
		if math.sqrt((self.y - ball.y) ** 2 + (self.x - ball.x) ** 2) < self.player_width/2 + ball.r:
			if self.touching_red_ball == False:
				self.score -= 10
				self.touching_red_ball = True
		else:
			self.touching_red_ball = False