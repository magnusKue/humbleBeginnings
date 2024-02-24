//pin 2-4 led 1-3: Lauflicht
int x=2;
void setup() {
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
}
void loop() {
  for (x=3;x<5;x++)
  {
    delay(200);
    digitalWrite(x, HIGH);
    delay(10);
    digitalWrite(x, LOW);
    
  }
  
  for (x=3;x>=2;x--)
  {
    delay(200);
    digitalWrite(x, HIGH);
    delay(10);
    digitalWrite(x, LOW);
    
  }
  
}
