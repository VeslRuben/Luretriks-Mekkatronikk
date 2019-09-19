
#include <Wire.h>
#include <L3G.h>
L3G gyro;




void setup() {
  Serial.begin(19200);
  Wire.begin();
  if (!gyro.init())
  {
    Serial.println("Failed to autodetect gyro type!");
    while (1);
  }

  gyro.enableDefault();
}

void loop() {
  gyro.read();
  Serial.print((int)gyro.g.x);
  Serial.print(" ");
  Serial.print((int)gyro.g.y);
  Serial.print(" ");
  Serial.println((int)gyro.g.z);
}
