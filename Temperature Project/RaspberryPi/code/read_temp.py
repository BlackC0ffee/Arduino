import serial
import time
import datetime
ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(3) #timeout of 3 seconds 
ser.write("1") #trigger the arduino to send temp 
temp = ser.readline() #read the temp 
dt = datetime.datetime.now() 
f = open("/home/pi/log/temperature.csv", "a")
f.write(dt.strftime("%d-%m-%Y,%H:%M") + "," + temp)
f.close();

