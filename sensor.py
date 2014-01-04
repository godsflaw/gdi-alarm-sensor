#!/usr/bin/env python

import RPi.GPIO as GPIO

class GDIAlarmSensor:
  """
  An GDIAlarmSensor class
  
  Usage: subclass the GDIAlarmSensor class and call run() when ready
  """
  def __init__(self, bouncetime, mode=GPIO.BCM):
    self.mode = mode
    self.bouncetime = bouncetime
    GPIO.setmode(mode)
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    def sprinkler_alarm(channel):
      print "sprinkler alarm detected on 17"
    def fire_alarm(channel):
      print "fire alarm detected on 23"
    GPIO.add_event_detect(17, GPIO.FALLING, callback=sprinkler_alarm, bouncetime=bouncetime)
    GPIO.add_event_detect(23, GPIO.FALLING, callback=fire_alarm,      bouncetime=bouncetime)

  def __del__(self):
    GPIO.cleanup()

  def run(self):
    while True:
      time.sleep(1)
