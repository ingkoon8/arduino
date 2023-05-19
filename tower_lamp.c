#define LAMP_RED  2
#define LAMP_YELLOW  3
#define LAMP_GREEN  4

#define RELAY_ON  1
#define RELAY_OFF 0

void setup() {
  pinMode(LAMP_RED,OUTPUT);
  pinMode(LAMP_YELLOW,OUTPUT);
  pinMode(LAMP_GREEN,OUTPUT);
  digitalWrite(LAMP_RED,RELAY_OFF);
  digitalWrite(LAMP_YELLOW,RELAY_OFF);
  digitalWrite(LAMP_GREEN,RELAY_OFF);
}

void loop() {
  digitalWrite(LAMP_RED,RELAY_ON);
  digitalWrite(LAMP_YELLOW,RELAY_OFF);
  digitalWrite(LAMP_GREEN,RELAY_OFF);
  delay(1000);
  digitalWrite(LAMP_RED,RELAY_OFF);
  digitalWrite(LAMP_YELLOW,RELAY_ON);
  digitalWrite(LAMP_GREEN,RELAY_OFF);
  delay(1000);
  digitalWrite(LAMP_RED,RELAY_OFF);
  digitalWrite(LAMP_YELLOW,RELAY_OFF);
  digitalWrite(LAMP_GREEN,RELAY_ON);
  delay(1000);
  digitalWrite(LAMP_RED,RELAY_OFF);
  digitalWrite(LAMP_YELLOW,RELAY_OFF);
  digitalWrite(LAMP_GREEN,RELAY_OFF);
  delay(1000);
}
