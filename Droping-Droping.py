import pygame
import random
import math
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Ball Game')

black = (0,0,0)
white = (249,248,113)
neg = (209,0,0)
pos = (0,200,150)
placlr = (255,138,119)
darkback = (53,53,53)

clock = pygame.time.Clock()
crashed = False
score = 0

hitimer = 0

helth = 5

gameoverornot = False

class ball:

	def __init__(self,x,y,spd):
		self.x = x
		self.y = display_height+100 
		self.colour = darkback
		self.size = 50
		self.speed = spd
		self.timer = 0
		self.typeof = 1 
		self.movevar = 1
		self.counter = 0
	def move(self):
		global score ,hitimer
		if (self.y - self.size > display_height) or self.y - self.size < -300:
			self.y = -200
			self.timer=0
			self.x = random.randint(0,display_width)
			self.speed = random.randint(3,12)
			self.size = int(self.speed*5)
			a = 255 - (self.speed*255)//12
			self.colour = (a,a,a)

			if self.speed > 8:
				x = random.random()
				if x > 0.5:
					self.typeof = 1
				else:
					self.typeof = 2
			else:
				self.typeof = 0

		self.y+=self.speed;
		if self.y > display_height//5:
			res = self.collision(pla.x,pla.y,pla.wid,20,self.x,self.y,self.size)
		else:
			res = False
		if res and self.timer<1:
			
			
			self.timer = 100

			if self.typeof == 0:
				score+=self.speed
				self.y = display_height+100
			elif self.typeof == 2:
				self.speed = -self.speed
				score-=(self.speed*2)
				#hitimer = 10
			else:
				global helth
				helth-=1
				self.y = display_height+100
				if  helth < 1:
					gameover()
				hitimer = 10
		self.counter +=1
		if self.counter %8 == 0:
			self.counter = 0
			if self.movevar == 0 :
				self.movevar = 1
			else:
				self.movevar = 0

		if self.timer>0:
			self.timer-=1


	def draw(self):
		if self.typeof  == 1:
			if self.movevar == 0:
				pygame.draw.line(gameDisplay, (0,0,0), (self.x-int(self.size*1.3), self.y), (self.x+int(self.size*1.3), self.y))
				pygame.draw.line(gameDisplay, (0,0,0), (self.x, self.y-int(self.size*1.3)), (self.x, self.y+int(self.size*1.3)))
			else:	
				pygame.draw.line(gameDisplay, (0,0,0), (self.x-int(self.size*1.2), self.y-int(self.size*1.2)), (self.x+int(self.size*1.2), self.y+int(self.size*1.2)))
				pygame.draw.line(gameDisplay, (0,0,0), (self.x-int(self.size*1.2), self.y+int(self.size*1.2)), (self.x+int(self.size*1.2), self.y-int(self.size*1.2)))
			pygame.draw.circle(gameDisplay, (0,0,0), (self.x, self.y), self.size+8,3)
			pygame.draw.circle(gameDisplay, self.colour, (self.x, self.y), self.size)
			pygame.draw.circle(gameDisplay, neg, (self.x, self.y), self.size-10)
		elif self.typeof  == 2:
			pygame.draw.circle(gameDisplay, self.colour, (self.x, self.y), self.size)
			pygame.draw.circle(gameDisplay, neg, (self.x, self.y), self.size-10)
		else:
			pygame.draw.circle(gameDisplay, self.colour, (self.x, self.y), self.size)
			pygame.draw.circle(gameDisplay, pos, (self.x, self.y), self.size-10)

	def collision(self,rleft, rtop, width, height,center_x, center_y, radius):  # circle definition
		rright, rbottom = rleft + width, rtop + height

		cleft, ctop     = center_x-radius, center_y-radius
		cright, cbottom = center_x+radius, center_y+radius

		if rright < cleft or rleft > cright or rbottom < ctop or rtop > cbottom:
			return False  

		for x in (rleft, rleft+width):
			for y in (rtop, rtop+height):
				if math.hypot(x-center_x, y-center_y) <= radius:
					return True  
		if rleft <= center_x <= rright and rtop <= center_y <= rbottom:
			return True  
		return False  

class player:
	def __init__(self):
		self.x = display_width//2-50
		self.y = display_height-20
		self.colour = placlr
		self.wid = 100
	def move(self,dire):

		if dire == "Right" and  self.x < (display_width-self.wid):
			self.x += 10
		elif dire == "Left" and self.x > 0:
			self.x -= 10
		else:
			self.x = self.x

	def draw(self):
		pygame.draw.rect(gameDisplay, (black), (self.x, self.y , self.wid,25))
		pygame.draw.rect(gameDisplay, self.colour, (self.x, self.y , self.wid,15))
		pygame.draw.polygon(gameDisplay, placlr, ((self.x, self.y),(self.x, self.y-(helth*10)),(self.x+50, self.y),(self.x+100, self.y-(helth*10)),(self.x+100, self.y)))

def gameover():
	global pause,score,helth,gameoverornot
	pause = True
	gameoverornot = True
	gameDisplay.fill(white)
	text2 = largeText.render("Game Over | "+str(score), True, neg, darkback)
	gameDisplay.blit(text2, ((display_width//2)-255,display_height//2-115,30,30)) 
	pygame.display.update()
	score = 0
	helth = 5

pla = player()
movedir = "none"
balls = []
for i in range(10):
	balls.append(ball(random.randint(0,display_width),-100,3))

pygame.init()

largeText  = pygame.font.SysFont("comicsansms", 65)
ScoreText  = pygame.font.SysFont("comicsansms", 32)
pause = False

while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				movedir = "Left"
			elif event.key == pygame.K_RIGHT:
				movedir = "Right"
			elif event.key == pygame.K_SPACE:
				if pause == True:
					pause = False
				else:
					pause = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				movedir = "none"
	if not pause:
		if hitimer == 0:
			gameDisplay.fill(white)
		else:
			gameDisplay.fill((255,10,10))

		if hitimer > 0 :
			hitimer -=1

		for b in balls:
			b.draw()

		pla.move(movedir)
		pla.draw()
		text = ScoreText.render(str(score), True, pos, darkback)
		gameDisplay.blit(text, (10,10,30,30)) 

		hel = ScoreText.render("<3 "*helth, True, pos, darkback)
		gameDisplay.blit(hel, ((display_width)-205,20,30,30)) 

		for b in balls:
			b.move()

	else:
		if not gameoverornot:
		#	print("="*50)
			gameDisplay.fill(white)

		text1 = largeText.render("|| Pause ||", True, pos, darkback)
		gameDisplay.blit(text1, ((display_width//2)-165,display_height//2-210,30,30)) 		

		text1 = largeText.render(" Droping-Droping ", True, pos, darkback)
		gameDisplay.blit(text1, ((display_width//2)-265,display_height//2-300,30,30)) 


		pygame.draw.rect(gameDisplay, (darkback), (200 ,280, 400 , 310))

		hel = ScoreText.render("Collect", True, pos, darkback)
		gameDisplay.blit(hel, ((display_width//2)-175,320,30,30)) 

		pygame.draw.circle(gameDisplay, (155,155,155), ((display_width//2)+70,330), 38)
		pygame.draw.circle(gameDisplay, pos, ((display_width//2)+70,330), 31)
		
		hel = ScoreText.render("Hit Back", True, pos, darkback)
		gameDisplay.blit(hel, ((display_width//2)-175,420,30,30)) 
		
		pygame.draw.circle(gameDisplay, (155,155,155), ((display_width//2)+70,430), 45)
		pygame.draw.circle(gameDisplay, neg, ((display_width//2)+70,430), 38)

		hel = ScoreText.render("Avoide", True, pos, darkback)
		gameDisplay.blit(hel, ((display_width//2)-175,520,30,30)) 

		pygame.draw.line(gameDisplay, (0,0,0), ((display_width//2)+10,530), ((display_width//2)+130,530))
		pygame.draw.line(gameDisplay, (0,0,0), ((display_width//2)+70,470), ((display_width//2)+70,590))
		pygame.draw.circle(gameDisplay, (0,0,0), ((display_width//2)+70,530), 48 , 2)
		pygame.draw.circle(gameDisplay, (155,155,155), ((display_width//2)+70,530), 42)
		pygame.draw.circle(gameDisplay, neg, ((display_width//2)+70,530), 34)




	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()

