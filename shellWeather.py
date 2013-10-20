import sys
import json
import urllib2

screen = [[' ' for j in range(80)]]
positions = [[2,2],[22,2],[42,2]]

def appendLine(n):
  for i in range(n):
    screen.append([' ' for j in range(80)])

def safedraw(x,y,char):
  if y + 1 > len(screen):
    appendLine(y + 1 - len(screen))
  if x >= 0 and x < len(screen[0]) and y >= 0:
    screen[y][x] = char

def drawstring(x,y,string):
  for char in enumerate(string):
    safedraw(x + char[0], y, char[1])
  return (x, y)

def drawascii(x,y,art):
  art = open('icons/' + art,'r')
  location = None
  for line in enumerate(art):
    location = drawstring(x,y + line[0],line[1].rstrip())
  return location

def displayWeather(n, forecast):
  art = forecast['icon']
  high = forecast['high']['fahrenheit']
  low = forecast['low']['fahrenheit']
  text = forecast['conditions']
  day = forecast['date']['weekday']
  x = positions[n][0]
  y = positions[n][1]

  drawstring(x + 5,y,day)
  y = (drawascii(x,y+2,art)[1] + 1)
  drawstring(x,y,text)
  drawstring(x,y+1,'high:' + high)
  drawstring(x+10,y+1,'low:' + low)

def printScreen():
  for line in screen:
    print "".join(line)

if __name__ =='__main__':
  if len(sys.argv) < 2 or not sys.argv[1].isdigit():
    sys.exit(1)
  zipcode = sys.argv[1]

  apikey = (open('api', 'r')).readline()
  getURL = json.load(urllib2.urlopen('http://api.wunderground.com/api/' + apikey + '/geolookup/q/' + zipcode + '.json'))['location']['requesturl'].split(".")[0]
  fullJson = json.load(urllib2.urlopen('http://api.wunderground.com/api/' + apikey + '/forecast/q/' + getURL + '.json'))
  threeDayForecast = fullJson['forecast']['simpleforecast']['forecastday']
  print zipcode
  for i in range(3):
    displayWeather(i, threeDayForecast[i])
  printScreen()