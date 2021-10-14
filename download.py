import os
import requests
from lxml import html
from urlparse import urlparse
import urllib

PAGES = 5
IMAGES_DIR = 'mecha_images/'
BASE_URL = 'https://acrylicosvallejo.com/en/categoria/hobby/mecha-color-en/page/'

def download_images():
    for i in range(1, PAGES + 1):
        download_page(i)

def download_page(page_number):
    page = requests.get(BASE_URL + str(page_number) + '/')
    tree = html.fromstring(page.content)

    images = tree.xpath("//img[@srcset]")

    for image in images:
        src = image.get('src')
        a = urlparse(src)
        filename = os.path.basename(a.path)
        print("Retreiving " + filename)
        urllib.urlretrieve(image.get('src'), os.path.join(IMAGES_DIR, filename))

if __name__ == "__main__":
    download_images()