import requests
import subprocess
from bs4 import BeautifulSoup

print 'Bird Song Scraper!'
url = 'http://macaulaylibrary.org/search?&recordist=Parker,%20Theodore%20A.,%20III&recordist_id=911'
r = requests.get(url)
html_doc = r.text

print(html_doc)

#wget http://audio.macaulaylibrary.org/8/83163.mp3
#curl -o test.mp3 http://audio.macaulaylibrary.org/8/83163.mp3
subprocess.call("curl -o test.mp3 http://audio.macaulaylibrary.org/8/83163.mp3", \
                shell=True)
sys.exit(0)