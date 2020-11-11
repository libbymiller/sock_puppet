#!/usr/bin/python
import subprocess
import sys
import time
import os
import traceback
import math

import threading

import pantilthat

import expressions/smile
import expressions/sad
import expressions/grin
import expressions/grimace
import expressions/question
import expressions/bit_sad
import expressions/small_neutral
import expressions/very_sad
import expressions/cross
import expressions/neutral
import expressions/tick
import expressions/speak1
import expressions/speak2

try:
    import numpy
except ImportError:
    exit("This script requires the numpy module\nInstall with: sudo pip install numpy")

speaking = False
t1 = None

def foo():
       global speaking
       for x in range(100):
         print(x)
         speak1.speak1()
         speak1.wait_clear(0.1)
         speak2.speak2()
         speak1.wait_clear(0.1)
         if(speaking == False):
            print("BREAK!")
            break

def smooth_pan(start,to,timeout=0.005):
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
 

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

class SimpleEcho(WebSocket):

    def handleMessage(self):
        global speaking
        global t1
        command = self.data
        print("command",command)

        if(command == "left_a_bit"):
          try:
            p = pantilthat.get_pan()
            print("p",p)
            smooth_pan(p,p+10)
          except:
            traceback.print_exc()

        if(command == "right_a_bit"):
          try:
            p = pantilthat.get_pan()
            print("p",p)
            smooth_pan(p,p-10)
          except:
            traceback.print_exc()

        if(command == "down_a_bit"):
          t = pantilthat.get_tilt()
          try:
            print("t - down a bit",t)
            smooth_tilt(t,t+10)
          except:
            traceback.print_exc()

        if(command == "up_a_bit"):
          t = pantilthat.get_tilt()
          try:
            smooth_tilt(t,t-10)
          except:
            traceback.print_exc()

        if(command == "stopspeaking"):
          speaking = False
          print("Got command stopspeaking",command)
          print("speaking is false")
          try:
            t1.join()
          except:
            traceback.print_exc()
          smile.smile()

        if(command == "speaking"):
          speaking = True
          print("Got command speaking")
          try:
             t1 = threading.Thread(target=foo, args=())
             t1.start()
          except:
            traceback.print_exc()

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
          smile.smile()
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


    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

server = SimpleWebSocketServer('', 80, SimpleEcho)
server.serveforever()

