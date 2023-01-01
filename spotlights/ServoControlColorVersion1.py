#-*- coding:UTF-8 -*-
# ##########################
#  Implement by pwm
# ##########################

import RPi.GPIO as GPIO
import time

#RGB Pi-Pin Code
LED_R = 22
LED_G = 27
LED_B = 24
SERVO = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# init output mode
def init():
    global pwm_servo
    GPIO.setup(LED_R, GPIO.OUT)
    GPIO.setup(LED_G, GPIO.OUT)
    GPIO.setup(LED_B, GPIO.OUT)
    GPIO.setup(SERVO, GPIO.OUT)

    # set pwm with 50hz
    pwm_servo = GPIO.PWM(SERVO, 50)
    pwm_servo.start(0)

	
# change color based on angle

def turn_on_red():
    GPIO.output(LED_R, GPIO.HIGH)
	GPIO.output(LED_G, GPIO.LOW)
	GPIO.output(LED_B, GPIO.LOW)

def turn_on_green():
    GPIO.output(LED_R, GPIO.LOW)
    GPIO.output(LED_G, GPIO.HIGH)
    GPIO.output(LED_B, GPIO.LOW)

def turn_on_blue():
    GPIO.output(LED_R, GPIO.LOW)
	GPIO.output(LED_G, GPIO.LOW)
	GPIO.output(LED_B, GPIO.HIGH)


def turn_on_red_green():
	GPIO.output(LED_R, GPIO.HIGH)
	GPIO.output(LED_G, GPIO.HIGH)
	GPIO.output(LED_B, GPIO.LOW)

def turn_on_green_blue():
	GPIO.output(LED_R, GPIO.LOW)
	GPIO.output(LED_G, GPIO.HIGH)
	GPIO.output(LED_B, GPIO.HIGH)

def turn_on_red_blue():
    GPIO.output(LED_R, GPIO.HIGH)
	GPIO.output(LED_G, GPIO.LOW)
	GPIO.output(LED_B, GPIO.HIGH)

def turn_on_red_green_blue():
    GPIO.output(LED_R, GPIO.HIGH)
	GPIO.output(LED_G, GPIO.HIGH)
	GPIO.output(LED_B, GPIO.HIGH)

def turn_off_red_green_blue():
    GPIO.output(LED_R, GPIO.LOW)
	GPIO.output(LED_G, GPIO.LOW)
	GPIO.output(LED_B, GPIO.LOW)



def corlor_light(angle):
    if angle > 150:
        turn_on_red()
    elif angle > 125:
        turn_on_red()
    elif angle >100:
        turn_on_blue()
    elif angle > 75:
        turn_on_red_green()
    elif angle > 50:
        turn_on_green_blue()
    elif angle > 25:
        turn_on_red_blue()
    elif angle > 0:
        turn_on_red_green_blue()
    else :
        turn_off_red_green_blue()
		
# servo turning
def servo_control_color():
    for angle in range(181):
        pwm_servo.ChangeDutyCycle(2.5 + 10 * angle/180)
        corlor_light(angle)
	    time.sleep(0.009) 
    
    for angle in reversed(range(181)):
        pwm_servo.ChangeDutyCycle(2.5 + 10 * angle/180)
	    corlor_light(angle)
	    time.sleep(0.009)

    time.sleep(2)


try:
    init()
    # init to move forward
    pwm_servo.ChangeDutyCycle(2.5 + 10 * 90/180)
    while True:
 	servo_control_color()
		
except KeyboardInterrupt:
    pass
pwm_servo.stop()
GPIO.cleanup()
