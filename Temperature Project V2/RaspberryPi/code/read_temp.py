import serial
import time
import datetime
ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(3) #timeout of 3 seconds 
ser.write("1") #trigger the arduino to send temp 
data = ser.readline() #read the data 
dt = datetime.datetime.now() 
f = open("/home/pi/log/temperatureData.csv", "a")
f.write(dt.strftime("%d-%m-%Y,%H:%M") + "," + data) # KISS, we just add the data at the end. :)
f.close();