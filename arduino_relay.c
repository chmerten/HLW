// Arduino code to control relays based on commands received from Python script

const int relayPin = 2; // Change this to the actual pin connected to the relay

void setup() {
  pinMode(relayPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    if (command.startsWith("1:ON")) {
      digitalWrite(relayPin, HIGH); // Turn relay on
      Serial.println("Relay 1 is ON");
    } else if (command.startsWith("1:OFF")) {
      digitalWrite(relayPin, LOW); // Turn relay off
      Serial.println("Relay 1 is OFF");
    }
  }
}
