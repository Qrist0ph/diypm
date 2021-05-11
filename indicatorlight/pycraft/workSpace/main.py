import urequests
import machine, neopixel
import time

np = neopixel.NeoPixel(machine.Pin(2), 16)
np[7] = (0, 0, 255)


def getData():
  response = urequests.get('http://app.diypm.space:9090/api_1/GetShortData?portfolioguid=LIVEDEMO----------------------------')

  print(type(response))


  print(response.text)
  print(type(response.text))

  parsed = response.json()
  print(type(parsed))

  depotwert_d=parsed["depotwert_d"]
  tagesgewinn_d=parsed["tagesgewinn_d"]
  
  ration =tagesgewinn_d/(depotwert_d-tagesgewinn_d)
  #print(parsed["title"])
  return ration*100
  
def connect():
    import network
 
    ssid = "your_2G_wifi"
    password =  "password"
 
    station = network.WLAN(network.STA_IF)
 
    if station.isconnected() == True:
        print("Already connected")
        return
 
    station.active(True)
    station.connect(ssid, password)
 
    while station.isconnected() == False:
        pass
 
    print("Connection successful")
    print(station.ifconfig())


def setColor(v):
  x=abs(v)
  c=0;
  if x<0.2:
    c=220
  elif x <0.5:
    c=180
  elif x < 0.8:
    c=150
  elif x < 1.1:
    c=100
  elif x < 1.8:
    c=50
  
  color=[c,c,c]
  if v < 0:
    color[0]=255
  else:
     color[1]=255
  
  print(color)
  np = neopixel.NeoPixel(machine.Pin(2), 16)
  for i in range(16):
    np[i] = color
  np.write()



while True:
  connect()
  x=getData()
  print(x)
  setColor(x)
  time.sleep(300) 


