import pygame
import time
import random
import threading
import sys

cell_size = 5
bgcolor = (0, 0, 0)
snake_color = (120, 214, 200)
sleep = .1
flag = False
bigfood_color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))

class snake(threading.Thread):
  def __init__(self):
    super(snake, self).__init__()
    self.array = [[100, 100], [100, 100-6]]
    self.running = True
    self.allowm = True
    self.dir = 'd'
    self.x = random.randint(20, cell_size * 60 -20)
    self.y = random.randint(20, cell_size * 60 -20)
    self.score = 0
    self.count = [0, 0]
    self.bigfud =[0, 0]
    self.tick = 0
    self.f = False
    self.food_color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    pygame.init()

    pygame.init()
    self.screen=pygame.display.set_mode((cell_size * 60, cell_size * 60))
    self.screen.fill(bgcolor)
    pygame.display.set_caption('Snake 1.0')
    pygame.draw.rect(self.screen, (255, 255, 255), (10, 20, cell_size * 60 - 20, cell_size * 60 - 30), 1)
    for i in self.array:
      (x, y) = i
      pygame.draw.circle(self.screen, snake_color, (x,y), cell_size, 0)  
    pygame.draw.circle(self.screen, self.food_color, (self.x, self.y), cell_size, 0)
    pygame.display.flip()  
    self.start()
  
  
  def over(self):
    f=pygame.font.SysFont("Arial", 15)
    t=f.render(' Game Over!!!  Your Score: %d' %self.score, True, (150, 150, 150))
    self.screen.blit(t, (50, 100))
    pygame.display.update()
    sys.exit(0)
    print 'Game Over!!!'
    print ' Your Score: %d' %self.score
    time.sleep(1)
    self.running = False

  def callrand(self):
    
    global bigfood_color
    self.x = random.randint(20, cell_size * 60 - 20)
    self.y = random.randint(30, cell_size * 60 - 20)
    self.food_color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    l = len(self.array)
    if self.dir == 'd':
      [tx, ty] = self.array[l - 1]
      self.array.append([tx, ty - cell_size])
    elif self.dir == 'u':
      [tx, ty] = self.array[l - 1]
      self.array.append([tx, ty + cell_size])
    elif self.dir == 'r':
      [tx, ty] = self.array[l - 1]
      self.array.append([tx - cell_size, ty])
    elif self.dir == 'l':
      [tx, ty] = self.array[l - 1]
      self.array.append([tx + cell_size, ty])
     
    self.count[0] += 1
    self.score += 10
    if self.count[0] % 5 == 0:
      self.f =True
      self.tick = 0
      self.bigfud[0] = random.randint(20, cell_size * 60 -20)
      self.bigfud[1] = random.randint(30, cell_size * 60 -20)
      bigfood_color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))  
 
  def checkcol(self):
    
    head = self.array[0]
    for j in range(1, len(self.array)):
      if head == self.array[j]:
	f = 0
	return f
    f = 1  
    return f  

  def plot(self):
 
    global bigfood_color
    head = self.array[0]
    if self.x in range(head[0] - cell_size, head[0] + cell_size) and self.y in range(head[1] - cell_size, head[1] + cell_size):
       self.callrand()
    f = self.checkcol()   
    self.screen.fill(bgcolor)
    pygame.draw.rect(self.screen, (255, 255, 255), (10, 20, cell_size * 60 - 20, cell_size * 60 - 30), 1)
    for i in self.array:
      (x, y) = i
      pygame.draw.circle(self.screen, snake_color, (x, y), cell_size, 0)
    pygame.draw.circle(self.screen, self.food_color, (self.x, self.y), cell_size, 0)
    f=pygame.font.SysFont("Arial", 10)
    t=f.render('Score: %d' %self.score, True, (150, 150, 150))
    self.screen.blit(t, (230, 5))
    pygame.display.update()
    if self.f == True and self.tick < 50:
      self.tick += 1
      pygame.draw.circle(self.screen, bigfood_color, (self.bigfud[0], self.bigfud[1]), cell_size * 2, 0)
      pygame.display.flip()
      if self.bigfud[0] in range(head[0]-cell_size*2, head[0]+cell_size*2) and self.bigfud[1] in range(head[1]-cell_size*2, head[1]+cell_size*2):
	self.tick = 70
	self.score += 25
	
    if f == 0:
      self.over()
 
  def move(self, direction):

   if self.dir <> direction:
      if not (self.dir == 'u' and direction == 'd'): 
        if not(self.dir == 'd' and direction == 'u'):
	  if not(self.dir == 'r' and direction == 'l'):
	    if not(self.dir == 'l' and direction == 'r'):
              self.dir = direction
   if self.dir == 'd':
      head = self.array[0]
      if head[1] < (cell_size * 60) -15 and self.allowm:
        c = 0
        s = []
        j = 0
        for i in self.array:
          s.append(i)
  
          if c == 0:
	    c += 1
          else:
	    self.array[j] = s[j - 1]
          j += 1
        [hx, hy] = self.array[0]
        hy += cell_size
        self.array[0] = [hx, hy]

        self.plot()
        time.sleep(sleep)

      else:
        self.allowm = False
        self.over()
      return

   elif self.dir == 'u':
      head = self.array[0]
      if head[1] > 25 and self.allowm:
        c = 0
        s = []
        j = 0
        for i in self.array:
          s.append(i)
  
          if c == 0:
	    c += 1
          else:
	    self.array[j] = s[j - 1]
          j += 1
        [hx, hy] = self.array[0]
        hy -= cell_size
        self.array[0] = [hx, hy]

        self.plot()
        time.sleep(sleep)

      else:
        self.allowm = False
        self.over()
      return

   elif self.dir == 'r':
      head = self.array[0]
      if head[0] < (cell_size * 60) - 15 and self.allowm:
        c = 0
        s = []
        j = 0
        for i in self.array:
          s.append(i)
  
          if c == 0:
	    c += 1
          else:
	    self.array[j] = s[j - 1]
          j+=1
        [hx, hy] = self.array[0]
        hx += cell_size
        self.array[0] = [hx, hy]

        self.plot()
        time.sleep(sleep)

      else:
        self.allowm = False
        self.over()
      return

   elif self.dir == 'l':
      head = self.array[0]
      if head[0] > 15 and self.allowm:
        c = 0
        s = []
        j = 0
        for i in self.array:
          s.append(i)
  
          if c == 0:
	    c += 1
          else:
	    self.array[j] = s[j - 1]
          j += 1
        [hx, hy] = self.array[0]
        hx -= cell_size
        self.array[0] = [hx, hy]

        self.plot()
        time.sleep(sleep)

      else:
        self.allowm = False
        self.over()
      return

class snakeconfig(threading.Thread):  
  
  s = snake()
  
  direction = 'd'
  s.move(direction)

  while s.running:
    s.move(direction)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        s.running = 0

      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
	  direction = 'd'
	  s.move(direction)

        elif event.key == pygame.K_UP:
	  direction = 'u'
	  s.move(direction)

        elif event.key == pygame.K_RIGHT:
	  direction = 'r'
	  s.move(direction)

        elif event.key == pygame.K_LEFT: 
	  direction= 'l'
	  s.move(direction)


def main():
  sc = snakeconfig()
  sc.start()

if __name__ == __main__:
  main()

