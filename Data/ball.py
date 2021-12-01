import pygame,os,time,random 

class Ball():
	def __init__(self,x,y,r,master,color):
		self.x = x 
		self.y = y 
		self.r = r 
		self.color = color
		self.master = master
		self.vx = random.randint(0,4) - 2
		self.vy = random.randint(0,4) - 2
		while self.vx == 0 or self.vy == 0:
			self.vx = random.randint(0,4) - 2
			self.vy = random.randint(0,4)
	def draw(self):
		pygame.draw.circle(self.master,self.color,(self.x,self.y),self.r)
	def move(self,dt):
		self.x += self.vx*dt
		self.y += self.vy*dt
		if self.x - self.r < 0:
			self.x = self.r
			self.vx *= -1
		elif self.x + self.r > 1000:
			self.x = 1000 - self.r
			self.vx *= -1
		if self.y - self.r < 0:
			self.y = self.r
			self.vy *= -1
		elif self.y + self.r > 700:
			self.y = 700 - self.r
			self.vy *= -1