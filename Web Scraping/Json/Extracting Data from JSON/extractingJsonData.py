import json
# import requests
import urllib
from urllib.request import urlopen

# Sample data - http://py4e-data.dr-chuck.net/comments_42.json
# Actual data - http://py4e-data.dr-chuck.net/comments_1269059.json

url = input('Enter Location: ')
data = urllib.request.urlopen(url).read()
data = json.loads(data)
count_list = [num['count'] for num in data['comments']]
print(sum(count_list))

"""
instead of urllib, we can use requests too to get the Json data

data = requests.get(url)
data = json.loads(data.text)
count_list = [num['count'] for num in data['comments']]
print(sum(count_list))
"""
