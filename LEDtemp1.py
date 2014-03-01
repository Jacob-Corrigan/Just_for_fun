#-------------------------------------------------------------------------------
# Name:        Tempature LED
# Purpose: Displayed the tempature by using LEDs and blinking intensity
#
# Author:      Zoae
#
# Created:     28/02/2014
# Copyright:   (c) Zoae 2014
# Licence:     1337Sauc3
#-------------------------------------------------------------------------------

import urllib2
import re
import time
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)
gpio.setup(23, gpio.OUT)
gpio.setup(24, gpio.OUT)
gpio.setup(25, gpio.OUT)

gpio.output(18, False)
gpio.output(23, False)
gpio.output(24, False)
gpio.output(25, False)

def temp_get():
    url = 'http://api.wunderground.com/api/3391e02e468c643c/conditions/q/GA/Roswell.xml'
    website = urllib2.urlopen(url).read()
    str_temp = re.search('<temp_f>'+"(.*?)"+'</temp_f>',website).group(1)
    int_temp = float(str_temp)
    return int_temp

def flash_calc(temp):
    if temp >= 100:
        return 60*5
    elif temp >= 72:
        y =0+(1-0)*(temp-72)/(100-72)
        return 1-y
    elif temp >= 68:
        return 60*10
    elif temp > 50:
        y =0+(1-0)*(temp-50)/(68-50)
        return y
    elif temp > 32:
        y =0+(1-0)*(temp-32)/(50-32)
        return y
    elif temp <= 32:
        return 60*10

while True:

    temp = float(temp_get())
    t = flash_calc(temp)

    if temp >= 100:
	print str(time.strftime("%H:%M:%S")) + " " + str(temp)
        t = flash_calc(temp)
        gpio.output(25, True)
        time.sleep(t)
        gpio.output(25, False)

    if temp >= 72:
        i=0
        t = flash_calc(temp)
	print str(time.strftime("%H:%M:%S")) + " " + str(temp)
        a=int((300/(flash_calc(temp))))
        for i in range(a):
            gpio.output(25, True)
            time.sleep(t)
            gpio.output(25, False)
            time.sleep(t)

    elif temp > 68:
	print str(time.strftime("%H:%M:%S")) + " " + str(temp)
        gpio.output(24, True)
        time.sleep(t)
        gpio.output(24, False)

    elif temp > 50:
        i=0
        t = flash_calc(temp)
        a=int((300/(flash_calc(temp))))
	print str(time.strftime("%H:%M:%S")) + " " + str(temp)
        for i in range(a):
            gpio.output(23, True)
            time.sleep(t)
            gpio.output(23, False)
            time.sleep(t)

    elif temp > 32:
        i=0
        t = flash_calc(temp)
        a=int((300/(flash_calc(temp))))
	print str(time.strftime("%H:%M:%S")) + " " + str(temp)
        for i in range(a):
            gpio.output(18, True)
            time.sleep(t)
            gpio.output(18, False)
            time.sleep(t)

    else:
	print str(time.strftime("%H:%M:%S")) + " " + str(temp)
        gpio.output(18, True)
        time.sleep(t)
        gpio.output(18, False)