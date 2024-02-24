int but1 = 2;
int but2 = 4;
void setup() {
  pinMode(but1, INPUT_PULLUP);
  pinMode(but2, INPUT_PULLUP);
}
void akt1() {
  digitalWrite(13, HIGH);
}
void akt2() {
  digitalWrite(13, LOW);
}

void loop() 
{
  if (digitalRead(bt1) == 0)
  { 
  akt1();
  }
  else
  {
  delay(10);
  }
  
  if (digitalRead(bt2) == 0)
  {
    akt2();
  }
  else
  {
    delay(10);
  }
}
    
    
  
