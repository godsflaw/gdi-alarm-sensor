#!/usr/bin/env python

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def sprinkler_alarm(channel):
  print "sprinkler alarm detected on 17"

def fire_alarm(channel):
  print "fire alarm detected on 23"

GPIO.add_event_detect(17, GPIO.FALLING, callback=sprinkler_alarm, bouncetime=300)
GPIO.add_event_detect(23, GPIO.FALLING, callback=fire_alarm,      bouncetime=300)

try:
  GPIO.wait_for_edge(24, GPIO.RISING)
  print ""

except KeyboardInterrupt:
  GPIO.cleanup()

GPIO.cleanup()
