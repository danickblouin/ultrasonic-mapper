#include "SR04.h"
#include "Servo.h"

#define TRIG_PIN 12
#define ECHO_PIN 11
SR04 sr04 = SR04(ECHO_PIN,TRIG_PIN);

Servo myServo;
#define SERVO_PIN 9

int distance;
int current_angle;
int init_angle = 0;
int max_angle = 180;
int increment_angle = 5;

void setup() {
	Serial.begin(9600);
	myServo.attach(SERVO_PIN);
	myServo.write(init_angle);
	delay(1000);
	Serial.println("-------");
	Serial.println(max_angle);
}

void loop() {
	int total = 0;
	int number = 10;
	for (int i = 0; i < 10; i++) {
		int dis = sr04.Distance();
		if (dis > 1000) {
			number--;
			continue;
		}
		total += dis;
		delay(100);
	}
	distance = total / number;
	// Serial.println("Distance: " + String(distance) + " Angle: " + String(current_angle));
	Serial.println(distance);
	current_angle += increment_angle;
	myServo.write(current_angle);
	delay(1000);
	if (current_angle > max_angle) {
		exit(0);
	}
}
