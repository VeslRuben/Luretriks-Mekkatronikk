#include <SoftwareSerial.h>
#include <math.h>
#include <VarSpeedServo.h>

VarSpeedServo servo0;
VarSpeedServo servo1;
VarSpeedServo servo2;

int A = 40;
float phi = (120.0 / 180.0) * M_PI;
int T = 1000;
int servSpeed = 0;

boolean goingForward = false;
boolean goingBackward = false;

int bluetoothTx = 2;

int bluetoothRx = 3;

SoftwareSerial bluetooth(bluetoothTx, bluetoothRx);


void setup() {
  // put your setup code here, to run once:
  servo0.attach(9);
  servo1.attach(10);
  servo2.attach(11);
  servo0.write(90);
  servo1.write(90);
  servo2.write(90);
  delay(1000);
  
  Serial.begin(9600);
  bluetooth.begin(115200);
  bluetooth.print("$");
  bluetooth.print("$");
  bluetooth.print("$");
  delay(100);
  bluetooth.println("U,9600,N");
  bluetooth.begin(9600);
}

void loop() {
    // put your main code here, to run repeatedly:
    if(bluetooth.available()) {
      char tempBlue = (char)bluetooth.read();
      Serial.println(tempBlue);
      if(tempBlue != -1) {
        if(tempBlue == 'v') {
          goLeft();
        } else if(tempBlue == 'h') {
          goRight();
        } else if(tempBlue == 'f') {
          goingForward = true;
          goingBackward = false;
        } else if(tempBlue == 'b') {
          goingForward = false;
          goingBackward = true;
        } else if(tempBlue == 'x') {
          goingForward = false;
          goingBackward = false;
        }
      }
    }
    if(Serial.available()) {
      bluetooth.print((char)Serial.read());
    }
    if(goingForward) {
      goForward();
    } else if(goingBackward) {
      goBackward();
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

void goLeft() {
  int y = servo2.read() + 15;
  if(y > 135) {
    y = 135;
  }
  servo2.write(y);
  Serial.println("Going left");
}

void goRight() {
  int y = servo2.read() - 15;
  if(y < 45) {
    y = 45;
  }
  servo2.write(y);
  Serial.println("Going right");
}

int updateAngle(float T, float phase, float A) {
  float y = A * sin(((2*M_PI) / T) * millis() + phase);
  return y;
}
