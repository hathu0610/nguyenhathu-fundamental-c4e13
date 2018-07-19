from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL
html_content = urlopen("https://www.apple.com/itunes/charts/songs/").read().decode('utf-8')

url = "https://www.apple.com/itunes/charts/songs/"

soup = BeautifulSoup(html_content, "html.parser")
ul = soup.find("ul","")
li_list = ul.find_all("li")
new_list =[]
for li in li_list:
    h4 = li.find("h4")
    a = h4.find("a")

    artist = a.string
    
    h3 = li.find("h3")
    a1 = h3.find("a")

    names = a1.string

    a_list = {
        "name": names,
        "artist": artist
    }
    new_list.append(a_list)
    options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1, # Tell downloader to download only the first entry (audio)
    'format': 'bestaudio/audio'
    }
    dl = YoutubeDL(options)
    dl.download([names + artist])


pyexcel.save_as(records=new_list, dest_file_name="ex1.xlsx")