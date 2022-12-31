#-*- coding:UTF-8 -*-
#implement by pwm
import RPi.GPIO as GPIO
import time

#RGB Pin Code
LED_R = 22
LED_G = 27
LED_B = 24

# Servo Pin Code
ServoPin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# init output mode
def init():
    global pwm_servo
    GPIO.setup(LED_R, GPIO.OUT)
    GPIO.setup(LED_G, GPIO.OUT)
    GPIO.setup(LED_B, GPIO.OUT)
    GPIO.setup(ServoPin, GPIO.OUT)
    #设置pwm引脚和频率为50hz
    pwm_servo = GPIO.PWM(ServoPin, 50)
    pwm_servo.start(0)

	
# change color based on angle
def corlor_light(pos):
    if pos > 150:
        GPIO.output(LED_R, GPIO.HIGH)
	GPIO.output(LED_G, GPIO.LOW)
	GPIO.output(LED_B, GPIO.LOW)
    elif pos > 125:
	GPIO.output(LED_R, GPIO.LOW)
	GPIO.output(LED_G, GPIO.HIGH)
	GPIO.output(LED_B, GPIO.LOW)
    elif pos >100:
        GPIO.output(LED_R, GPIO.LOW)
	GPIO.output(LED_G, GPIO.LOW)
	GPIO.output(LED_B, GPIO.HIGH)
    elif pos > 75:
	GPIO.output(LED_R, GPIO.HIGH)
	GPIO.output(LED_G, GPIO.HIGH)
	GPIO.output(LED_B, GPIO.LOW)
    elif pos > 50:
	GPIO.output(LED_R, GPIO.LOW)
	GPIO.output(LED_G, GPIO.HIGH)
	GPIO.output(LED_B, GPIO.HIGH)
    elif pos > 25:
        GPIO.output(LED_R, GPIO.HIGH)
	GPIO.output(LED_G, GPIO.LOW)
	GPIO.output(LED_B, GPIO.HIGH)
    elif pos > 0:
        GPIO.output(LED_R, GPIO.HIGH)
	GPIO.output(LED_G, GPIO.HIGH)
	GPIO.output(LED_B, GPIO.HIGH)
    else :
        GPIO.output(LED_R, GPIO.LOW)
	GPIO.output(LED_G, GPIO.LOW)
	GPIO.output(LED_B, GPIO.LOW)
		
# servo turning
def servo_control_color():
    for pos in range(181):
        pwm_servo.ChangeDutyCycle(2.5 + 10 * pos/180)
	corlor_light(pos)
	time.sleep(0.009) 
    for pos in reversed(range(181)):
        pwm_servo.ChangeDutyCycle(2.5 + 10 * pos/180)
	corlor_light(pos)
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
