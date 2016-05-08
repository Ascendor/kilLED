#!/usr/bin/env python

from SourceLib import SourceLog
import asyncore
import subprocess
import socket
import json
from datetime import datetime


# create a sourcelogparser
class LEDLogParser(SourceLog.SourceLogParser):

    def action(self, remote, timestamp, key, value, properties):
                                
                                
#        device.show_message(key, font=proportional(CP437_FONT), delay=0.2)

#        try:
#        print(key)
#        print(value)
#        print(properties)

        self.my_action(remote, timestamp, key, value, properties)
#        except:
#            print("ERROR")
#            pass

    def my_action(self, remote, timestamp, key, value, properties):
        print(key)
        print(value)
        if key == 'kill':
            device.show_message(value['attacker_name'] + " killed " + value['victim_name'], font=proportional(CP437_FONT), delay=0.03)


try:
    import max7219.led as led
    import time
    import SourceLib
    from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT
    from random import randrange

    device = led.matrix5x7(cascaded=8, vertical=True)
    device.brightness(15)
    device.show_message("kilLED", font=proportional(CP437_FONT), delay=0.07)
    time.sleep(1)

    ip = '192.168.188.22'
    server = SourceLog.SourceLogListener((ip, 17015), ('192.168.188.21', 27015), LEDLogParser())

    asyncore.loop()
 

except KeyboardInterrupt:
    print "terminating..."
#except:
#    print "General exception"
finally:
    device.clear()
    


