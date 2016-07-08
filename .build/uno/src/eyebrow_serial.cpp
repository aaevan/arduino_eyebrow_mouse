#include <Arduino.h>
#include "pitches.h"
void setup();
void loop();
#line 1 "src/eyebrow_serial.ino"
//#include "pitches.h"

// set pin numbers for the five buttons:
const int LeftSwitch = 5;
const int MiddleSwitch = 6;
const int RightSwitch = 7;
const int BuzzerPin = 3;

const int LED1 = 13;     // the number of the pushbutton pin
const int LED2 = 12;     // the number of the pushbutton pin
const int LED3 = 11;     // the number of the pushbutton pin

int delay_time = 100;

void setup() {
  // initialize the buttons' inputs:
  pinMode(LeftSwitch, INPUT);
  pinMode(MiddleSwitch, INPUT);
  pinMode(RightSwitch, INPUT);
  pinMode(BuzzerPin, OUTPUT);

  pinMode(LED1,      OUTPUT); 
  pinMode(LED2,      OUTPUT); 
  pinMode(LED3,      OUTPUT); 
  Serial.begin(9600);
}

void loop() {
  // read the buttons:
  int LeftState = digitalRead(LeftSwitch);
  int MiddleState = digitalRead(MiddleSwitch);
  int RightState = digitalRead(RightSwitch);
  
  if (LeftState == HIGH){
    digitalWrite(LED1, HIGH);
  }
  else{
    digitalWrite(LED1, LOW);
  }
  if (MiddleState == HIGH){
    digitalWrite(LED2, HIGH);
  }
  else{
    digitalWrite(LED2, LOW);
  }
  if (RightState == HIGH){
    digitalWrite(LED3, HIGH);
  }
  else{
    digitalWrite(LED3, LOW);
  }

  // calculate the movement distance based on the button states:
  if(LeftState == LOW && MiddleState == LOW && RightState == LOW){
    tone(BuzzerPin, NOTE_C4);
  }
  else if(LeftState == LOW && MiddleState == LOW && RightState == HIGH){
    tone(BuzzerPin, NOTE_D4);
  }
  else if(LeftState == LOW && MiddleState == HIGH && RightState == LOW){
    tone(BuzzerPin, NOTE_E4);
  }
  else if(LeftState == LOW && MiddleState == HIGH && RightState == HIGH){
    tone(BuzzerPin, NOTE_F4);
  }
  else if(LeftState == HIGH && MiddleState == LOW && RightState == LOW){
    tone(BuzzerPin, NOTE_G4);
  }
  else if(LeftState == HIGH && MiddleState == LOW && RightState == HIGH){
    tone(BuzzerPin, NOTE_A5);
  }
  else if(LeftState == HIGH && MiddleState == HIGH && RightState == LOW){
    tone(BuzzerPin, NOTE_B5);
  }
  else if(LeftState == HIGH && MiddleState == HIGH && RightState == HIGH){
    tone(BuzzerPin, NOTE_C5);
  }
  // a delay so the mouse doesn't move too fast:
  delay(100);
  Serial.print(LeftState * 1);
  Serial.print(MiddleState * 2);
  Serial.print(RightState * 4);
  Serial.print(" ");
  Serial.print("\n");
}
