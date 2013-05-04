import requests
import subprocess
import sys

def download(mp3_link, local_fname):
  print 'Downloading: ' + mp3_link
  command = ' '.join(['curl', '-o', download_dir + local_fname, mp3_link])
  subprocess.call(command, shell=True)
  

download_dir = 'downloads/'

#typical response
#

url = 'http://macaulaylibrary.org/search?&recordist=Parker,%20Theodore%20A.,%20III&recordist_id=911'
r = requests.get(url)
html_doc = r.text
print html_doc
sys.exit(0)

mp3_link = 'http://audio.macaulaylibrary.org/7/72788.mp3'
download(mp3_link, 'second_test.mp3')


