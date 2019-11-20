int x =0;

void setup() {
  size(600, 600);
  background(127);
  //this line is for the speed
  frameRate(20);
}
void draw() {
  //add background to wipe the repeatation of the object
  background(127);  
  rect(x, 100, 100, 400);
  x = x + 1;
  //x = x + 5;
}
