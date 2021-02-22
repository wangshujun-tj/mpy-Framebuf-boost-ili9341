import sys
import os,network
import machine
import socket
import time
from machine import I2C,Pin,RTC
import ntptime
SSID="ssid"
PASSWORD="password"
wlan=None
def connectWifi(ssid,passwd):
  global wlan
  cnt=0
  print("Start Wifi  NIC.")
  wlan=network.WLAN(network.STA_IF)                     #create a wlan object
  wlan.active(True)                                     #Activate the network interface
  print("Connect Wifi.",end="")
  wlan.disconnect()                                     #Disconnect the last connected WiFi
  wlan.connect(ssid,passwd)                             #connect wifi
  while(not wlan.isconnected()):
    time.sleep(0.5)
    print(".",end="")
  print(" OK")
  print("IP ADDR:",wlan.ifconfig())  
  return True
connectWifi(SSID,PASSWORD)

rtc = RTC()
ntptime.host = "ntp.aliyun.com"
ntptime.NTP_DELTA -= 8*3600
ntptime.settime()

print(rtc.datetime())




