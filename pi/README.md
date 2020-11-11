# Introduction

The idea is that you run a headless browser on the pi, and connect to it 
via a laptop or phone using a browser. 

You'll need a [server](/server) to connect to first.

# Installation

This is mostly a matter of making sure the audio and video drivers are 
in place, and then running chromium on boot, together with a simple 
python websockets server for controlling the pan-tilt hat and 5*5 led 
matrix.

## Set up the Pi with Buster (not Buster-lite, and not Stretch)

[Here are full instructions for burning an SD 
card](https://www.raspberrypi.org/documentation/installation/installing-images/) 
or use [Etcher](https://etcher.io).

When it's done, do

    touch /Volumes/boot/ssh

[Add in your wifi network 
creds](https://www.raspberrypi.org/blog/page/2/?fish#another-update-raspbian) 
to /Volumes/boot/wpa_supplicant.conf:

    nano /Volumes/boot/wpa_supplicant.conf

contents (the country first line is important, though it doesn't have to 
be GB, obviously):

     country=GB
     ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
     update_config=1

     network={
       ssid="foo"
       psk="bar"
     }


Eject the SD card and put it in a Pi3.

Log in, e.g. by using a screen and keyboard and mouse or by sharing your 
network over ethernet and sshing in, or sshing in over your network if 
you added the credentials beforehand.

## Add audio and video drivers

    sudo nano /etc/modules

contents:

    i2c-dev
    snd-bcm2835
    bcm2835-v4l2


## Enable USB audio

    sudo nano /boot/config.txt 

in contents

    #dtparam=audio=on ## comment this out

then

    sudo nano /lib/modprobe.d/aliases.conf

in contents

    #options snd-usb-audio index=-2 # comment this out

## Give the GPU more oomph

This is optional, but you'll get smoother video performance at the cost 
of the chip getting hotter...! ([more 
info](https://raspberrypi.stackexchange.com/a/1885)).

Edit config.txt

    sudo pico /boot/config.txt  

contents - add or edit:

    gpu_mem=192 

## Add autostart

    sudo nano /etc/xdg/lxsession/LXDE-pi/autostart

contents:

    @lxpanel --profile LXDE-pi
    @pcmanfm --desktop --profile LXDE-pi
    @xscreensaver -no-splash
    @xset s off
    @xset -dpms
    @xset s noblank
    @/bin/bash /home/pi/start_all.sh

if you need to rotate the camera (as you will if using the pan-tilt 
hat, as it places it upside down), put

    v4l2-ctl --set-ctrl-rotate=270                                           

into `sudo nano /etc/rc.local`

Add the files start_all.sh and server.py from this directory into the pi 
homedirectory. Edit ```start_all.sh``` to refer to your server.

Make them executable:

    chmod a+x start_all.sh 

install the python dependencies (as sudo because we run it as sudo, 
because it's port 80)

    sudo pip install pantilthat SimpleWebSocketServer

enable the camera and serial in ```interfaces``` using

    sudo raspi-config

Change the pi name and password

    sudo nano /etc/hostname
    sudo nano /etc/hosts
    passwd

## Assemble everything

Shutdown and unplug the pi, then - 

 * connect the pi camera
 * connect the tilt-pan hat
 * connect the 5*5 led matrix
 * plug in the pi's power again

Connect to https://your-server:8443/remote.html on a laptop, 
ideally in Chrome. You should see whatever the Pi's camera is pointing at, 
and be able to hear too, and speak. 

Longer term, you need to figure out how to do notifications. There's a 
place in [server.js](/../server/server.js) where you can send a dm tweet, 
for example.

