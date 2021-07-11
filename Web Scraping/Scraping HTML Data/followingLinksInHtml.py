from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re

try:
    url = input('Enter URL: ')
    count = int(input('Enter Count: '))
    position = int(input('Enter position: '))

    for each in range(count):
        html = urlopen(url)
        bs = BeautifulSoup(html, 'html.parser')
        href_list = bs.find_all('a')                    # href_list will have all the href links
        href_tag = href_list[position - 1]              # finding the url for the mentioned position
        href_pattern = r'href="(.+)"'
        name_pattern = r'">(.+)</a>'
        url = ''.join(re.findall(href_pattern, str(href_tag)))      # assigning the url for iteration
        name = ''.join(re.findall(name_pattern, str(href_tag)))
    print(name)

except HTTPError as e:
    print(e)
except URLError as e:
    print(e)
