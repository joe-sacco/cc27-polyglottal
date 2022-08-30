// Code below adapted from https://www.arduino.cc/en/Tutorial/BuiltInExamples/AnalogReadSerial

/*
  AnalogReadSerial

  Reads an analog input on pin 0, prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  
*/

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0); 
  // print out the value you read:
  sensorValue = sensorValue - 11; // sensor range offset
  Serial.println(constrain(sensorValue, 0, 127)); // constrained to MIDI note range
  //Serial.println(sensorValue);
  delay(50);        // delay in between reads for stability
}