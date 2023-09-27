int red_led = 13
int yellow_led = 12

void setup() {
  // put your setup code here, to run once:
pinMode(red_led, OUTPUT)
pinMode(yellow_led, OUTPUT)
}

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(red_led, HIGH)
delay(600)
digitalWrite(red_led, LOW)
delay(600)

digitalWrite(yellow_led, HIGH)
delay(600)
digitalWrite(yellow_led, LOW)
delay(600)
}
