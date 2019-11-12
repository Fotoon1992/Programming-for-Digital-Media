int[] nums = {20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10};
void setup() {
  size(800, 600);
}
void draw(){
  background(255);
  for(int circle = 0 ; circle <= 10 ; circle = circle + 1) {
  ellipse(((780/10) * circle), 10 + ((580/10) * circle), nums[circle], nums[circle]);
  fill(0);
}
}
