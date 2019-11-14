#******************************
# (3-1 and 3-2) I added the function event that has the color yellow to change the red car when the user presses space
# (3-3) I added new objects as a trees
# (3-4) the mousepressed works 'as adding lakes'
# (3-5) I added a ellipse and if the user pressed 'a' it will change to square 'as a traffic rotary'
#********************************

class Car(object):  

    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        
    def event(self):
        stroke(0)
        fill(self.c - 100)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 20, 10)
        
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 20, 10)
    
    def drive(self):
        self.xpos = self.xpos + self.xspeed
        if self.xpos > width:
            self.xpos = 0
            
class newObject(object):
    
    def __init__(self, c, xpos, ypos):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
    
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 20, 10)
    
class creation(object):
    
    def __init__(self, c, mx, my):
        self.c = c
        self.mX = 0
        self.mY = 0
        
      #creat new function that relocates the mousex and mousey then call it in draw 
    def update(self, mx,my):
        self.mX = mx
        self.mY = my
    
    def display(self):
        stroke(0)
        fill(self.c)
        ellipseMode(CENTER)
        ellipse(self.mX, self.mY, 30, 30)
        
myCar1 = Car(color(255, 0, 0), 0, 100, 2)    
myCar2 = Car(color(0, 255, 255), 0, 10, 1)
#mynewObject2 = newObject(color(0, 255, 0), 20, 60)
#mynewObject3 = newObject(color(0, 255, 0), 180, 160)
#mynewObject4 = newObject(color(0, 255, 0), 130, 150)
#mynewObject5 = newObject(color(0, 255, 0), 50, 70)
#mycreation = creation(color(0, 0, 0), mouseX, mouseY)
#newrandom = ([mynewObject1], [mynewObject2], [mynewObject3], [mynewObject4], [mynewObject5])

#same thing as in last lab using array with append
#trees in fall season
arr = []
for i in range(10):
    arr.append(newObject(color(random(255), 255, 0), random(200), random(200)))
for i in range(10):
    arr.append(newObject(color(random(255), 140, 0), random(200), random(200)))
    
def setup():
    size(200,200)
    
#cookie and the cookie cutter
create = creation(color(73, 63, 253),0,0)

def draw():
    background(255)
    
    fill(0)
    textSize(20)
    text("Press a", 70, 190)
    
    #displaying the array here
    for i in arr:
        i.display()
        
    create.display()
    #mynewObject1.display()
    #mynewObject2.display()
    #mynewObject3.display()
    #mynewObject4.display()
    #mynewObject5.display()
    #newObject.display
    myCar1.drive()
    myCar1.display()
    myCar2.drive()
    myCar2.display()
              
    if ((keyPressed) and (key == 'a')):
      fill(120, 51, 0)
      square(100, 70 ,50)
    else:
      fill(120, 51, 0)
      ellipse(100, 70, 40, 40)
        
    if ((keyPressed) and (key == ' ')):
        myCar1.event()
    #pass
#create lakes
def mousePressed():
    create.update(mouseX,mouseY)
         #fill(0, 0, 240)
         #ellipse(mouseX, mouseY, 20, 20)
  