import requests
from bs4 import BeautifulSoup
import os


def create_repo(folder):
  os.mkdir(os.path.join(os.getcwd(), folder))

def imageDownloader(url, folder):
    try:
        create_repo(folder)
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    for image in images:
        name = image['alt']
        link = image['src']
        with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('Writing: ', name)

          
def main():
  imageDownloader('https://www.airbnb.co.uk/s/Paris--France/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&place_id=ChIJl2HKCjaJbEcRaEOI_YKbH2M&query=Paris%2C%20France&checkin=2020-11-01&checkout=2020-11-22&source=search_blocks_selector_p1_flow&search_type=search_query', 'paris')

main()
