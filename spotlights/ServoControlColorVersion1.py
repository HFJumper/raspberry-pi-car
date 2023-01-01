# -*- coding:UTF-8 -*-
# ##########################
#  Implement by pwm
# ##########################

import RPi.GPIO as GPIO
import time

# RGB Pi-Pin Code
LED_R = 22
LED_G = 27
LED_B = 24
SERVO = 23


class SpotLightManager:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(LED_R, GPIO.OUT)
        GPIO.setup(LED_G, GPIO.OUT)
        GPIO.setup(LED_B, GPIO.OUT)
        GPIO.setup(SERVO, GPIO.OUT)
        self.pwm_servo = GPIO.PWM(SERVO, 50)
        self.pwm_servo.start(0)

    def turn_on_red(self):
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.LOW)

    def turn_on_green(self):
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.HIGH)
        GPIO.output(LED_B, GPIO.LOW)

    def turn_on_blue(self):
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)

    def turn_on_red_green(self):
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.HIGH)
        GPIO.output(LED_B, GPIO.LOW)

    def turn_on_green_blue(self):
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.HIGH)
        GPIO.output(LED_B, GPIO.HIGH)

    def turn_on_red_blue(self):
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)

    def turn_on_red_green_blue(self):
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.HIGH)
        GPIO.output(LED_B, GPIO.HIGH)

    def turn_off_red_green_blue(self):
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.LOW)

    def corlor_light(self, angle):
        if angle > 150:
            self.turn_on_red()
        elif angle > 125:
            self.turn_on_red()
        elif angle >100:
            self.turn_on_blue()
        elif angle > 75:
            self.turn_on_red_green()
        elif angle > 50:
            self.turn_on_green_blue()
        elif angle > 25:
            self.turn_on_red_blue()
        elif angle > 0:
            self.turn_on_red_green_blue()
        else:
            self.turn_off_red_green_blue()

    # servo turning
    def servo_control_color(self):
        for angle in range(181):
            self.pwm_servo.ChangeDutyCycle(2.5 + 10 * angle/180)
            self.corlor_light(angle)
            time.sleep(0.009)

        for angle in reversed(range(181)):
            self.pwm_servo.ChangeDutyCycle(2.5 + 10 * angle/180)
            self.corlor_light(angle)
            time.sleep(0.009)

        time.sleep(2)


if __name__ == "__main__":
    try:
        spot_light_manager = SpotLightManager()
        spot_light_manager.pwm_servo.ChangeDutyCycle(2.5 + 10 * 90/180)

        while True:
            spot_light_manager.servo_control_color()

    except KeyboardInterrupt:
        pass

    spot_light_manager.pwm_servo.stop()
    GPIO.cleanup()
