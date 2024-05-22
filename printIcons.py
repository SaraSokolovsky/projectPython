import requests
import urllib.request
from PIL import Image
import Exceptions as e
def load():
    global api,lst
    try:
        api = requests.get('https://api.github.com/emojis')
        lst = dict(api.json())
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        raise e



def print_all_icons():
    i = 1
    for l in lst.keys():
        print(i, ": ", l)
        i = i + 1
    return list(lst.keys())

def search_icons_by_keyword():
    global my_str
    str=input("search icons by  keyword\n")
    my_str=str.lower()
    list_search = list(filter(search,lst.keys()))
    if len(list_search)==0:
        raise e.NoResults("no result")
    else:
        i = 1
        for l in list(list_search):
            print(i, ": ", l)
            i = i + 1
    return list_search

def search(key):
    return my_str in str(key).lower()
def display_icon(i):
    try:
        urllib.request.urlretrieve(lst[i], "image.png")
        img = Image.open("image.png")
        img.show()
    except urllib.error.URLError as e:
        print("An error occurred:", e)
        raise e

