from bs4 import BeautifulSoup
import requests

class Top_100:
    def __init__(self,my_date):
        self.url = f" https://www.billboard.com/charts/japan-hot-100/{my_date}"
        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
        self.response = requests.get(self.url,headers=self.header)
        self.my_music_mood()
        
    def my_music_mood(self):
        self.soup = BeautifulSoup(self.response.text,"html.parser")
        self.titles = self.soup.select(selector="li h3")
        self.selection = [n.get_text().strip() for n in self.titles]
        self.selection = self.selection[:100]
        return self.selection


