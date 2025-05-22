from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    except URLError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

if __name__ == "__main__":
    url = input("Enter the HTML URL: ")
    title = getTitle(url)
    if title is None:
        print("Title could not be found")
    else:
        print("Title found:", title.get_text())