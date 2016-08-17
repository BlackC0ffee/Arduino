#include "DHT.h"

#define DHTPIN 2     // what digital pin we're connected to
#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321

// Initialize DHT sensor.
// Note that older versions of this library took an optional third parameter to
// tweak the timings for faster processors.  This parameter is no longer needed
// as the current DHT reading algorithm adjusts itself to work on faster procs.
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {

  if (Serial.available()) {

  //Waiting for trigger:
  Serial.read();
  
  float h = dht.readHumidity(); //Humidity
  float t = dht.readTemperature(); //Temperature (in Celsius)
  
  if (isnan(h) || isnan(t)) {
    Serial.println("Null");
    return;
  }

  float hic = dht.computeHeatIndex(t, h, false); //heatindex in Celsius


  // returns Humidity;Temperature;Heatindex
  Serial.print(h);
  Serial.print(",");
  Serial.print(t);
  Serial.print(",");
  Serial.println(hic);

  }
}