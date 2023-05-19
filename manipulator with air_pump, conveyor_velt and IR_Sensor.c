/*********************************************************************
1. sh1106 검색
2. adafruit 라이브러리 설치
*********************************************************************/

#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SH110X.h>
#include <Servo.h>

#define i2c_Address 0x3c

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels
#define OLED_RESET -1   //   QT-PY / XIAO
Adafruit_SH1106G display = Adafruit_SH1106G(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

#define VR_1  A0
#define VR_2  A1
#define VR_3  A2
#define BUTTON  A3  

bool state = 0;

#define SERVO_1 9
#define SERVO_2 8
#define SERVO_3 7
Servo servo_1;
Servo servo_2;
Servo servo_3;

#define PUMP_PIN  6
#define SOLVALVE_PIN  10
Servo servo_pump;
Servo servo_solvalve;

unsigned long currTime = 0;
unsigned long prevTime = 0;

void setup()   {
  Serial.begin(9600);
  
  pinMode(BUTTON,INPUT_PULLUP);

  delay(250); // wait for the OLED to power up
  display.begin(i2c_Address, true); // Address 0x3C default

  servo_1.attach(SERVO_1);
  servo_2.attach(SERVO_2);
  servo_3.attach(SERVO_3);

  servo_pump.attach(PUMP_PIN);
  servo_solvalve.attach(SOLVALVE_PIN);
  servo_pump.write(0);
  servo_solvalve.write(0);
}


void loop() {
  int vr_1,vr_2,vr_3;
  vr_1 = analogRead(VR_1);
  vr_2 = analogRead(VR_2);
  vr_3 = analogRead(VR_3);

  vr_1 = map(vr_1, 0, 1023, 180, 0);
  vr_2 = map(vr_2, 0, 1023, 180, 0);
  vr_3 = map(vr_3, 0, 1023, 180, 0);

  servo_1.write(vr_1);
  servo_2.write(vr_2);
  servo_3.write(vr_3);

  if(button_on() == 1){
    state = !state;

    if(state == 1){ // 물건 들기
      servo_solvalve.write(0); //공기 풀기
      servo_pump.write(180); ////펌프 가동 빨아들이기
      delay(200);
      servo_pump.write(0); //펌프 멈춤
    }
    else{ //물건 놓기
      servo_solvalve.write(180);
    }
  }

  currTime = millis();
  if(currTime - prevTime >= 1000)
  {
    prevTime = currTime;
    if(state == 1)
    {
      servo_solvalve.write(0); //공기 풀기
      servo_pump.write(180); ////펌프 가동 빨아들이기
      delay(200);
      servo_pump.write(0); //펌프 멈춤
    }
  }
  
  
  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(SH110X_WHITE);
  display.setCursor(0, 0);
  display.print("VR1: "); display.println(vr_1);
  display.print("VR2: "); display.println(vr_2);
  display.print("VR3: "); display.println(vr_3);
  display.print("BUTTON: "); display.println(state);
  display.display();
  
}

int button_on(){
  static int prevBtn = 1;
  static int currBtn = 1;
  currBtn = digitalRead(BUTTON);
  if(currBtn != prevBtn){
    prevBtn = currBtn;
    delay(100);
    if(currBtn == 0)  return 1;
  }

  return 0;
}
