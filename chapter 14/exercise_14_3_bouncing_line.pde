int x =0;
float xpos;
float xspeed = 2.8;
int xdirection = 1;

void setup() {
  size(100, 100);
  background(127);
  //this line is for the speed
  frameRate(20);
  xpos = width/2;
}
void draw() {
  //add background to wipe the repeatation of the object
  background(127);
  
   xpos = xpos + (xspeed * xdirection);
  
  if (xpos > width-x || xpos < x) {
    xdirection *= -1;
  }
  //rect(floatx, floaty,float width, flaot height)
  rect(xpos, 20, x, 50);
  //x = x + 1;
  //x = x + 5;
}
