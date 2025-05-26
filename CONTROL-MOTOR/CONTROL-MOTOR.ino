//#define ENA 5
#define IN1 4
#define IN2 5

void setup() {
  //pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim();

    if (command == "ON") {
      digitalWrite(IN1, HIGH);
      digitalWrite(IN2, LOW);
      analogWrite(ENA, 200);
    } else if (command == "OFF") {
      analogWrite(ENA, 0);
    } /*else if (command.startsWith("SPD:")) {
      int spd = command.substring(4).toInt();
      analogWrite(ENA, spd);
    }*/ else if (command == "DIR:F") {
      digitalWrite(IN1, HIGH);
      digitalWrite(IN2, LOW);
    } else if (command == "DIR:R") {
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, HIGH);
    }
  }
}
