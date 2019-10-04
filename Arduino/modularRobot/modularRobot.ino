#include <math.h>
#include <VarSpeedServo.h>

VarSpeedServo servo0;
VarSpeedServo servo1;
VarSpeedServo servo2;

int A = 40;
float phi = (120.0 / 180.0) * M_PI;
int T = 1000;
int servSpeed = 0;
boolean turned = false;
boolean going = false;


void setup() {
  servo0.attach(9);
  servo1.attach(10);
  servo2.attach(11);

  
  Serial.begin(9600);
  
  servo0.write(90);
  servo1.write(90);
  servo2.write(90);
  delay(1000);

  
}

void loop() {
  if(going) {
    if(millis() < 7000) {
      goBackward();
    }
    if (millis() > 3000 && !turned) {
      servo2.write(110);
      turned = true;
    }
    if(millis() > 7000 && turned) {
      goForward();
    }
  } else {
    lateralShift();
  }
}

void goForward() {
  servo0.write(90 + updateAngle(T, 0, A), servSpeed);
  servo1.write(90 + updateAngle(T, phi, A), servSpeed);
}

void goBackward() {
  servo0.write(90 + updateAngle(T, 0, A), servSpeed);
  servo1.write(90 + updateAngle(T, -phi, A), servSpeed);
}

void lateralShift() {
  servo0.write(90 + updateAngle(T, 0, A), servSpeed);
  servo1.write(90 + updateAngle(T, ((0.0/ 180) * M_PI), A), servSpeed);
  servo2.write(90 + updateAngle(T, ((-90.0/180.0) * M_PI), A), servSpeed);
}

int updateAngle(float T, float phase, float A) {
  float y = A * sin(((2*M_PI) / T) * millis() + phase);
  return y;
}
