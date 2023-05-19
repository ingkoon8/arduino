#include <Servo.h>

Servo servoSpin;
Servo servoArmRight;
Servo servoArmLeft;
Servo pumpServo;
Servo magServo;

#define SERVO_SPIN_PIN        2
#define SERVO_ARM_RIGHT_PIN   3
#define SERVO_ARM_LEFT_PIN    4
#define PUMP_MOTOR_PIN        5
#define PUMP_UNLOCK_PIN       6
#define JOYSTICK_LEFT_X       A0
#define JOYSTICK_LEFT_Y       A1
#define JOYSTICK_RIGHT_X      A2
#define JOYSTICK_RIGHT_Y      A3
#define SWITCH_PIN            12

#define STOP  0
#define UP    1
#define DOWN  2
#define LEFT  3
#define RIGHT 4

int leftJoyStickValue = STOP;
int rightJoyStickValue = STOP;

uint8_t spinServoValue = 90;
uint8_t leftServoValue = 90;
uint8_t rightServoValue = 90;

#define ON  1
#define OFF 0
uint8_t pumpOnOff = ON;

unsigned long prevTime = 0;
unsigned long currTime = 0;

void setup() {
  Serial.begin(9600);

  pinMode(SWITCH_PIN, INPUT);

  //3축 회전 서보 설정
  servoSpin.attach(SERVO_SPIN_PIN);
  servoArmLeft.attach(SERVO_ARM_LEFT_PIN);
  servoArmRight.attach(SERVO_ARM_RIGHT_PIN);
  servoSpin.write(90);
  servoArmRight.write(90);
  servoArmLeft.write(90);

  //펌프모터 서보설정
  pumpServo.attach(PUMP_MOTOR_PIN);
  magServo.attach(PUMP_UNLOCK_PIN);
  pumpServo.write(0);
  magServo.write(0);
}

void loop() {

  currTime = millis();
  if (currTime - prevTime >= 10)
  {
    prevTime = currTime;

    int leftX = analogRead(JOYSTICK_LEFT_X);
    int leftY = analogRead(JOYSTICK_LEFT_Y);
    int rightX = analogRead(JOYSTICK_RIGHT_X);
    int rightY = analogRead(JOYSTICK_RIGHT_Y);

    if (leftX >= 512 + 200)  leftJoyStickValue = UP;
    else if (leftX <= 512 - 200) leftJoyStickValue = DOWN;
    else if (leftY >= 512 + 200) leftJoyStickValue = LEFT;
    else if (leftY <= 512 - 200) leftJoyStickValue = RIGHT;
    else  leftJoyStickValue = STOP;

    if (rightX >= 512 + 200)  rightJoyStickValue = UP;
    else if (rightX <= 512 - 200) rightJoyStickValue = DOWN;
    else if (rightY >= 512 + 200) rightJoyStickValue = LEFT;
    else if (rightY <= 512 - 200) rightJoyStickValue = RIGHT;
    else  rightJoyStickValue = STOP;


    if (leftJoyStickValue == UP) {
      leftServoValue = constrain(leftServoValue - 1, 30, 120);
    }
    else if (leftJoyStickValue == DOWN) {
      leftServoValue = constrain(leftServoValue + 1, 30, 120);
    }
    else if (leftJoyStickValue == LEFT) {
      spinServoValue = constrain(spinServoValue + 1, 60, 120);
    }
    else if (leftJoyStickValue == RIGHT) {
      spinServoValue = constrain(spinServoValue - 1, 60, 120);
    }

    if (rightJoyStickValue == UP) {
      rightServoValue = constrain(rightServoValue - 1, 70, 150);
    }
    else if (rightJoyStickValue == DOWN) {
      rightServoValue = constrain(rightServoValue + 1, 70, 150);
    }

    Serial.print("L="); Serial.print(leftServoValue);
    Serial.print("\tS="); Serial.print(spinServoValue);
    Serial.print("\tR="); Serial.println(rightServoValue);

    servoArmLeft.write(leftServoValue);
    servoSpin.write(spinServoValue);
    servoArmRight.write(rightServoValue);
  }


  if (swOn() == 1)
  {
    if (pumpOnOff == ON)
    {
      Serial.println("pump On");
      magServo.write(180);
      delay(50);
      pumpServo.write(180);
      delay(1000);
      magServo.write(0);
      delay(50);
      pumpServo.write(0);
      pumpOnOff = OFF;
    }
    else if (pumpOnOff == OFF)
    {
      Serial.println("pump Off");
      magServo.write(180);
      pumpOnOff = ON;
    }

    delay(200); //채터링 방지
  }
}



uint8_t swOn()
{
  static uint8_t oldSw = 0;
  static uint8_t newSw = 0;
  newSw = digitalRead(SWITCH_PIN);
  if (newSw != oldSw)
  {
    oldSw = newSw;
    if (newSw == 1) return 1;
  }

  return 0;
}
