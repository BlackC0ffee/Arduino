/* Temperature Project */

#define aref_voltage 5 //Using 3.3 volts

//TMP36 Pin variables
int tempPin = 0;
int counter = 0;
int tempReading;

void setup() {
  // Sending Debug info to the serial monitor
  Serial.begin(9600);

  //SThis part is for 3.3v
  //analogReference(EXTERNAL);

}

void loop() {

  if (Serial.available()) {

  //Waiting for trigger:
  Serial.read();

  tempReading = analogRead(tempPin); // Reading the temprature

  //converting to Voltage
  float voltage = tempReading * aref_voltage;
  voltage /= 1024.0;

  float temperatureC = (voltage - 0.5) * 100 ;
  Serial.println(temperatureC);

  }

}
