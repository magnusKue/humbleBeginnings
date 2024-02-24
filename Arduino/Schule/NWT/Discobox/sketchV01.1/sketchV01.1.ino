/*<----------------------------discobox------------------------------------------------->
- by Maximilian Schied &&
Magnus Küderli
- Code written by Magnus K.
- 21.10.2020
- V1.1
*/
#define rgb11 1
#define rgb12 1 // (info: 1 led ist ja kaputt)

#define rgb21 1
#define rgb22 1
#define rgb23 1

#define danceFloor1 1
#define danceFloor2 1
#define danceFloor3 1
#define danceFloor4 1
#define danceFloor5 1
#define danceFloor6 1
#define danceFloor7 1
#define danceFloor8 1
/*
 <<<<<<<<<<Colors>>>>>>>>>>
 Colors:
 blue:  rgb(0, 255, 255)
 green: rgb(140, 255, 0)
 red:   rgb(230, 0, 0)
 idk:   rgb(255, 0, 191)
 yellow:rgb(255, 255, 0)
 white: rgb(255, 255, 255)
 <<<<<<<<<<<<<>>>>>>>>>>>>>
 */
//-------------variables-------------->
const float SPEED = 2.5;
int pins[13] = { rgb11, rgb12, rgb21, rgb22, rgb23, danceFloor1, danceFloor2, danceFloor3, danceFloor4, danceFloor5, danceFloor6, danceFloor7, danceFloor8} ; 

void setup() {
  //<--------------init-------------->
  randomSeed(analogRead(5));
  Serial.begin(9600);
  //<------define pins as output------>
  for (int num = 0; num < (sizeof(pins)/2); num++) {  
    pinMode(pins[num], OUTPUT);
    //Serial.println(pins[num]); //<debug>
  }
  //Serial.println((sizeof(pins)/2)); //<debug>
}

void loop() {
  //<-------------effects------------->
  for (int num = 0; num < (sizeof(pins)/2); num++) {  
    analogWrite(pins[num], 255);
    pinMode(num, OUTPUT);
    long col = random(5);
  }

  rgb(1,2,3, 255, 255, 255);
  delay(SPEED);
}

void rgb(int red, int green, int blue, int pinr, int ping, int pinb) {
  analogWrite(red, pinr);
  analogWrite(green, ping);
  analogWrite(blue, pinb);
}
