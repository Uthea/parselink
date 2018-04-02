import requests
import re
import os
from bs4 import BeautifulSoup


url = 'https://hi10anime.com/wp-login.php'  # hi10anime login page
payload = {'log': '', 'pwd': '', 'redirect_to': 'https://hi10anime.com/?p=44103'}  # log for username and pwd for password (chage redirect_to as desired also)


def loginToWeb(payload):
    """login to website using requests to generate the html file of page which contains the download link"""
    r = requests.post(url, data=payload)
    soup = BeautifulSoup(r.content, "lxml")

    if soup.find(string=re.compile("Username or Email Address")):
        print('Username or Password is invalid')
        return

    with open('file.html', 'bw') as f:
        f.write(r.content)

    parseLink()


def parseLink():
    """ parse download links using from file and find the correct download links using regex"""
    with open('file.html', 'br') as file:
        soup = BeautifulSoup(file, 'lxml')

        for line in soup.find_all('a'):
            links = str(line.get('href'))
            pattern = re.compile(r"http://bc.vc.+(hi10anime.+\.mkv)") #change regex query as suited

            if re.findall(pattern, links):
                print('http://' + re.findall(pattern, links)[0])

    os.remove('file.html')


loginToWeb(payload)