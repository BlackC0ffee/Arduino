# Temperature Project V2

## Wiring of the board

> todo

## Arduino Code

Download the folder Arduino/Temperature and upload it to the Arduino board. After the initialization the board will wait for input as trigger. Once the trigger has been given it returns a cvs-value as <Humidity>,<Temperature>,<Heat Index>. (e.g.: 40.80;25.10;24.73
)

## Raspberry PI

### Sending mail on Boot-up

See: http://cagewebdev.com/raspberry-pi-sending-emails-on-boot/

### Reading the Temperature

*Note:* This has been developed on Raspberry Pi Model B Revision 2.0 with Linux version 4.4.13+

In the current setup the Raspberry Pi uses a cron job to execute a script and sending a trigger to the Arduino (over USB), wait for the Arduino to return data and write it to a log.

1. Download RaspberryPi/code/read_temp.py to /home/pi/code/
2. Create a cron job with `crontab -e`, in our example we pull the data every 15 minutes.

```bash
0,15,30,45   *    *    *    *  python /home/pi/code/read_temp.py
```

Data can be found in /home/pi/log/temperatureData.csv