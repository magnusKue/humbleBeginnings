
int led = 13;
int bt1 = 2;
void setup() {                
  
  pinMode(led, OUTPUT);     
  pinMode(bt1, INPUT_PULLUP);     
}
void loop() 
{
  if (digitalRead(bt1) == 0)
  {
    digitalWrite(led, HIGH);  
  }
  else
  {
    digitalWrite(led, LOW);
  } 
}
