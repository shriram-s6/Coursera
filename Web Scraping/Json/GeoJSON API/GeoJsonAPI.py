import json
import urllib.request
import urllib.error
import urllib.parse

try:
    url = 'http://py4e-data.dr-chuck.net/json?'
    address = input('Enter location: ')

    if len(address) < 1:
        print('Enter valid location')                   # Universidad Central de Venezuela
    else:
        payload = {'key': 42, 'address': address}
        url = url + urllib.parse.urlencode(payload)
        data = urllib.request.urlopen(url).read()
        js_data = json.loads(data)
        place_id = js_data['results'][0]['place_id']
        print(place_id)                                 # ChIJky9zq9BYKowRQJOcyaRjBFU

except urllib.error.HTTPError as e:
    print(e)
except urllib.error.URLError as e:
    print(e)
