import requests
from bs4 import BeautifulSoup
import os
from time import sleep

i = 0

while i <10:

    res = requests.get('https://www.gocomics.com/pearlsbeforeswine/')
    res.raise_for_status()
    soup = BeautifulSoup(res.text)

    comic_div = soup.select 

    image_url = 'https:' + comic_div[0].contents[1].attrs['src']
    image_res = requests.get(image_url)

    image_file = open(os.path.basename(image_url), 'wb') #save just the file image name
    for chunk in image_res.iter_content(100000):
      image_file.write(chunk)
    image_file.close()

    i += 1

