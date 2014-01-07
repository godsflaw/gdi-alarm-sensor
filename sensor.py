#!/usr/bin/env python

import time
import smtplib
import RPi.GPIO as GPIO

from email.mime.text import MIMEText

class GDIAlarmSensor:
  """
  An GDIAlarmSensor class
  
  Usage: subclass the GDIAlarmSensor class and call run() when ready
  """
  def __init__(self, stime=30000, ftime=300000, mode=GPIO.BCM):
    self.mode = mode
    self.ftime = ftime
    self.stime = stime
    GPIO.setmode(mode)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    def fire_alarm(channel):
      msg = MIMEText('fire alarm detected on GPIO 17')
      msg['Subject'] = "FIRE ALARM"
      self.sendmail(msg)
    def sprinkler_alarm(channel):
      msg = MIMEText('sprinkler alarm detected on GPIO 23')
      msg['Subject'] = "SPRINKLER ALARM"
      self.sendmail(msg)
    GPIO.add_event_detect(17, GPIO.FALLING, callback=fire_alarm,      bouncetime=ftime)
    GPIO.add_event_detect(23, GPIO.FALLING, callback=sprinkler_alarm, bouncetime=stime)

  def __del__(self):
    GPIO.cleanup()

  def run(self):
    while True:
      time.sleep(1)

  def sendmail(self, msg):
    sender = 'chris@dod.net'
    recipients = ['2074502332@txt.att.net','2074086257@txt.att.net']
    msg['From'] = sender
    msg['To'] = '"Undisclosed recipients" <chris@dod.net>'
    smtp = smtplib.SMTP('mx.txt.att.net')
    smtp.sendmail(sender, recipients, msg.as_string())
    smtp.quit()
