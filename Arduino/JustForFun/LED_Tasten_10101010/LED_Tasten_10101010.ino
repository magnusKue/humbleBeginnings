int led = 13;
int btL = 2;
boolean ledstate = false;

void setup() 
{
  pinMode(led, OUTPUT);
  pinMode(btL, INPUT_PULLUP);
}

void loop()
{
  if (digitalRead(btL) == 0)
  {
    ledstate = !ledstate;
  }
  digitalWrite(led, ledstate);
  delay(250);
}
  
