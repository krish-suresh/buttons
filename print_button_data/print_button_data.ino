int button_pin = 2;
void setup() {
  pinMode(button_pin, INPUT);
  Serial.begin(9600);

}

void loop() {
  Serial.println(digitalRead(button_pin));
}
