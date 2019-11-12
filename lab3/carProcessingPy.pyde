#******************************
# (3-1 and 3-2) I added the function event that has the color yellow to change the red car when a the user press space
# (3-3) I added new objects but I could not do it with random 'as a trees'
# (3-4) the mousepressed works 'as adding lakes' but I needed to comment out the background to display the lakes and that will cause the cars to be unclear 
# (3-5) I added a ellipse and if the user press a it will change to square 'as a traffic rotary'
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
    
    def __init__(self, c, mouseX, mouseY):
        self.c = c
        self.mouseX = mouseX
        self.mouseY = mouseY
    
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.mouseX, self.mouseY, 20, 10)
        
myCar1 = Car(color(255, 0, 0), 0, 100, 2)    
myCar2 = Car(color(0, 255, 255), 0, 10, 1)
mynewObject1 = newObject(color(0, 255, 0), 10, 50)
mynewObject2 = newObject(color(0, 255, 0), 20, 60)
mynewObject3 = newObject(color(0, 255, 0), 180, 160)
mynewObject4 = newObject(color(0, 255, 0), 130, 150)
mynewObject5 = newObject(color(0, 255, 0), 50, 70)
#mycreation = creation(color(0, 0, 0), mouseX, mouseY)
#newrandom = ([mynewObject1], [mynewObject2], [mynewObject3], [mynewObject4], [mynewObject5])
def setup():
    size(200,200)
    '''for i in range(100):
        newobject = random(newrandom)'''

    
def draw():
    background(255)
    fill(0)
    textSize(30)
    text("Press a", 70, 190)
    mynewObject1.display()
    mynewObject2.display()
    mynewObject3.display()
    mynewObject4.display()
    mynewObject5.display()
    newObject.display
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
    pass
    
def mousePressed():
         fill(0, 0, 240)
         ellipse(mouseX, mouseY, 20, 20)
  
