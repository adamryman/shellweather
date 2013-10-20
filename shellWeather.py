import sys
import json
import urllib2

if __name__ =='__main__':
  if len(sys.argv) < 2 or not sys.argv[1].isdigit():
    sys.exit(1)
  zipcode = sys.argv[1]

  apikey = (open('api', 'r')).readline()

  getURL = json.load(urllib2.urlopen('http://api.wunderground.com/api/' + apikey + '/geolookup/q/' + zipcode + '.json'))['location']['requesturl'].split(".")[0]

  fullJson = json.load(urllib2.urlopen('http://api.wunderground.com/api/' + apikey + '/forecast/q/' + getURL + '.json'))

  forecasts = fullJson['forecast']['simpleforecast']['forecastday']