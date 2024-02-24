//test.ino

void setup() {
  pinMode(2, OUTPUT);
  Serial.begin(9600);
  Serial.println("1");
}

void loop() {
  Serial.println("test");
}