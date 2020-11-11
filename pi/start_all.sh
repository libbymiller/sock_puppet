#!/bin/bash

myrandom=$RANDOM
echo $myrandom

# kill any remaining bits
pkill -o chromium
sudo pkill -o websocketServer.py

# this is only needed for testing
export DISPLAY=:0.0

# sometimes useful to kill the whole profile
#rm -rf /home/pi/.config/chromium/

# this is for bad crashes, which leave a lock handing round
rm /home/pi/.config/chromium/SingletonLock

# run the server
sudo python /home/pi/websocketServer.py &

sleep 10

# run the browser
# It does seem to need to be kiosk, else the audio may not get picked up
/usr/bin/chromium-browser  --kiosk --disable-infobars --use-fake-ui-for-media-stream --disable-session-crashed-bubble --no-first-run --allow-running-insecure-content --allow-insecure-localhost https://libbybot.example.com:8443/libbybot/bot.html#$myrandom 
