def setup():
    
    size(750, 610)
    background(0,180,196)
    
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    
    #pointed up triangle
    a = createShape()
    a.beginShape()
    a.noFill()
    a.stroke(random(255))
    a.strokeWeight(4)
    a.vertex(0, -45)
    a.vertex(-35, 40)
    a.vertex(0, 30)
    a.vertex(35, 40)
    a.endShape(CLOSE)
    
    #pointed down triangle
    b = createShape()
    b.beginShape()
    b.noFill()
    b.stroke(random(255))
    b.strokeWeight(4)
    b.vertex(-40, -22)
    b.vertex(0, 30)
    b.vertex(40, -22)
    b.endShape(CLOSE)
    
    #up right ellipse
    c = createShape(ELLIPSE, -38, 6, 15, 15)
    c.setFill(color(random(255)))
    c.stroke(random(255))
    c.strokeWeight(5)
    
    #central up ellipse
    d = createShape(ELLIPSE, 0, -5, 15, 15)
    d.setFill(color(random(255)))
    d.stroke(random(255))
    d.strokeWeight(5)
    
    #bottom right ellipse
    e = createShape(ELLIPSE, -38, 22, 7, 7)
    e.setFill(color(random(255)))
    e.stroke(random(255))
    e.strokeWeight(5)
    
    #bottom central ellipse
    f = createShape(ELLIPSE, 0, 12, 10, 10)
    f.setFill(color(random(255)))
    f.stroke(random(255))
    f.strokeWeight(5)
    
    #rectanagle
    g = createShape(RECT, -40, -33, 8, 8)
    g.setFill(color(random(255)))
    g.stroke(random(255))
    g.strokeWeight(5)

def draw():

    translate(40, 45)
    shape(a)

    background(0,180,196)
    
    for i in range(20):
        for j in range(20):
            shape(a, i*75, j*75)
            shape(b, i*75, j*75)
            shape(c, i*75-2+(random(4)-1), j*75-2+(random(4)-1))
            shape(d, i*75-2+(random(4)-1), j*75-2+(random(4)-1))
            shape(e, i*75-2+(random(4)-1), j*75-2+(random(4)-1))
            shape(f, i*75-2+(random(4)-1), j*75-2+(random(4)-1))
            shape(g, i*75-2+(random(20)-9), j*75)
            
    # if statment to show the original shape (unit)
    if (mousePressed == True):
        translate(mouseX, mouseY)
        background(0,180,196)
        shape(a, 0, 0)
        shape(b, 0, 0)
        
    else:
        return
        
        
               
   
    #_______________________________________
    # I was trying to manipulate the colors of strok and fill  
    #_______________________________________      
   # arr = []
    #for i in range(10):
     #   for j in range(10):
            #shape(a, i*10, j*10)
      #      a.stroke(color(196,0,109))
      #      arr.append(shape(a, random(i), random(j)))
           # b.fill(color(196,0,109))
       #     arr.append(shape(b, i*5, j*5))
            #arr.append(shape(a, i*50, j*50))
            #arr.append(shape(b, i*50, j*50))
    #for i in range(5):
        #for j in range(5):
            #shape(a, i*30, j*30)
      #a.setFill(color(0))
    #else:
     #  fill(0)
