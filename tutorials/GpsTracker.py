import serial,time
import pynmea2
from threading import Timer

ser = 0
latitude=''
longitude=''

def init_serial():
    global ser
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = '/dev/serial0'
    
    ser.timeout = 1
    ser.open() 

    if ser.isOpen():
        print 'Open: ' + ser.portstr


def do_this():
     
     print 'latitude\t\tlongitude'
     print str(latitude)+'\t\t'+str(longitude)
     print ' '

     if latitude!='':
	     	gpslogger = open("gpslog.txt", "w")
	     	gpslogger.write(str(latitude)+','+str(longitude)+'\r\n')
	     	gpslogger.close()

   	
     t = Timer(5, do_this)
     t.start()
     
    

init_serial()
t = Timer(5, do_this)
t.start()


while 1:
	if ser.inWaiting() > 0 :
	    	recv=ser.readline()
		
		if recv.find('$GPGGA')!=-1:
			msg=pynmea2.parse(recv)
			print msg.timestamp
			latitude=msg.latitude
			longitude=msg.longitude
