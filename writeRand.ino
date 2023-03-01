#include <stdlib.h>

int rando;

void setup()
{    
  Serial.begin(9600);   
}

void loop()
{
  
  rando = (int) random(0,50);
  Serial.println(rando);
  delay(1000);  

}
