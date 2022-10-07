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
  //read the input on analog pin 0:
  int sensorValue1 = analogRead(A0);
  //print out the value you read:
  sensorValue1 = sensorValue1 - 11; // sensor range offset

  Serial.println(constrain(sensorValue1, 0, 100)); // constrained for parsing by 10 later in Python
  delay(50);        // delay in between reads for stability
}

