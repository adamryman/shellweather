import sys
import json
import urllib2

screen = [[' ' for j in range(80)] for k in range(50)]

def safeDraw(x,y,char):
  if x >= 0 and x < len(screen[0]) and y >= 0 and y < len(screen):
    screen[y][x] = char

def drawLine(x,y,string):
  for char in enumerate(string):
    safeDraw(x + char[0], y, char[1])

def drawAscii(x,y,art):
  art = open('icons/' + art,'r')
  for line in enumerate(art):
    drawLine(x,y + line[0],line[1])

if __name__ =='__main__':
  if len(sys.argv) < 2 or not sys.argv[1].isdigit():
    sys.exit(1)
  zipcode = sys.argv[1]

  apikey = (open('api', 'r')).readline()

  getURL = json.load(urllib2.urlopen('http://api.wunderground.com/api/' + apikey + '/geolookup/q/' + zipcode + '.json'))['location']['requesturl'].split(".")[0]

  fullJson = json.load(urllib2.urlopen('http://api.wunderground.com/api/' + apikey + '/forecast/q/' + getURL + '.json'))

  threeDayForecast = fullJson['forecast']['simpleforecast']['forecastday']