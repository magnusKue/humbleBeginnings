
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif
#define PIN 5
#define NUMPIXELS 21
Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
int delayval = 500;
void setup()
{
  pixels.begin();
  pixels.setPixelColor(0, pixels.Color(0,1,0));
  pixels.setPixelColor(1, pixels.Color(0,2,0)); 
  pixels.setPixelColor(2, pixels.Color(1,4,0));
  pixels.setPixelColor(3, pixels.Color(2,7,0));  
  pixels.setPixelColor(4, pixels.Color(4,10,0));
  pixels.setPixelColor(5, pixels.Color(7,12,0)); 
  pixels.setPixelColor(6, pixels.Color(10,15,0)); 
  pixels.setPixelColor(7, pixels.Color(12,17,0)); 
  pixels.setPixelColor(8, pixels.Color(15,20,0)); 
  pixels.setPixelColor(9, pixels.Color(17,29,0)); 
  pixels.setPixelColor(10, pixels.Color(20,50,0)); 
  pixels.setPixelColor(11, pixels.Color(17,29,0)); 
  pixels.setPixelColor(12, pixels.Color(15,20,0));
  pixels.setPixelColor(13, pixels.Color(12,15,0)); 
  pixels.setPixelColor(14, pixels.Color(10,15,0));  
  pixels.setPixelColor(15, pixels.Color(7,12,0)); 
  pixels.setPixelColor(16, pixels.Color(4,10,0));
  pixels.setPixelColor(17, pixels.Color(2,7,0)); 
  pixels.setPixelColor(18, pixels.Color(1,4,0));
  pixels.setPixelColor(19, pixels.Color(0,2,0)); 
  pixels.setPixelColor(20, pixels.Color(0,1,0));
  pixels.show();
}
void loop()
{
  delay(1000);
}


