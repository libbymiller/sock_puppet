#!/usr/bin/python
from bottle import run, route, request, response
import subprocess
import sys
import time
import os

import math
import time

import pantilthat

# http://stackoverflow.com/questions/10125881/send-a-message-from-javascript-running-in-a-browser-to-a-windows-batch-file
# e.g. curl --data 'command=left' -X POST http://localhost:8080/

def smooth_pan(start,to,timeout=0.005):
#  print("start pan",start,"to",to)
  count = start
  if(start > to):
    while count > to:
     count = count - 1
     pantilthat.pan(count)
     time.sleep(timeout)
  else:
    while count < to:
      count = count + 1
      pantilthat.pan(count)
      time.sleep(timeout)

def smooth_tilt(start,to,timeout=0.005):
#  print("start tilt",start,"to",to)
  count = start
  if(start > to):
    while count > to:
      count = count - 1
      pantilthat.tilt(count)
      time.sleep(timeout)
  else:
    while count < to:
      count = count + 1
      pantilthat.tilt(count)
      time.sleep(timeout)
 

@route('/', method=['OPTIONS', 'POST'])
def index():

    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

    command = "none"

    if request.method == 'POST':
      command = request.POST['command']
      print command
      arduino_command = None
      if(command):

# used by the software mostly
        if(command == "gone"):
          t = pantilthat.get_tilt()
          p = pantilthat.get_pan()
          smooth_tilt(t,80)
          smooth_pan(t,0)

        if(command == "arrived"):
          t = pantilthat.get_tilt()
          p = pantilthat.get_pan()
          smooth_tilt(t,0)
          smooth_pan(t,0)

# used by the end user / frontend

        if(command == "hello"):
          t = pantilthat.get_tilt()
          smooth_tilt(t,40,0.01)
          smooth_tilt(40,-70,0.01)
          smooth_tilt(-70,0,0.01)

        if(command == "leaving"):
          t = pantilthat.get_tilt()
          smooth_tilt(t,90)

        if(command == "left"):
          p = pantilthat.get_pan()
          smooth_pan(p,60)

        if(command == "right"):
          p = pantilthat.get_pan()
          smooth_pan(p,-60)

        if(command == "left_a_bit"):
          p = pantilthat.get_pan()
          smooth_pan(p,p+10)

        if(command == "right_a_bit"):
          p = pantilthat.get_pan()
          smooth_pan(p,p-10)

        if(command == "down_a_bit"):
          t = pantilthat.get_tilt()
          print("t - down a bit",t)
          smooth_tilt(t,t+10)

        if(command == "up_a_bit"):
          t = pantilthat.get_tilt()
          smooth_tilt(t,t-10)

        if(command == "halt"):
          t = pantilthat.get_tilt()
          p = pantilthat.get_pan()
          smooth_tilt(t,80)
          smooth_pan(p,0)
          # sleep
          time.sleep(5)
          result = os.system("sudo halt")
        if(command == "reboot"):
          t = pantilthat.get_tilt()
          p = pantilthat.get_pan()
          smooth_tilt(t,80)
          smooth_pan(p,0)
          time.sleep(5)
          result = os.system("sudo reboot")

    response.set_header('Access-Control-Allow-Origin', '*')
    result = "ok: "+command
    return result

run(host='localhost', port=8080, reloader=True)
