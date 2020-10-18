import cfscrape
from bs4 import BeautifulSoup
import re


class ModScraper:
    def __init__(self, version):
        self.version = version

    def get_mod_download_page(self, mod_name):

        DOWNLOAD_PAGE_URL = f"https://www.curseforge.com/minecraft/mc-mods/{mod_name}/files/all"

        scraper = cfscrape.create_scraper()
        r = scraper.get(DOWNLOAD_PAGE_URL)

        print(r.url)
        return r.text

    def parse_html(self, mod_page):
        pattern = f"{self.version}.\d"
        find_version = re.compile(pattern)
        soup = BeautifulSoup(mod_page, 'html.parser')
        v_divs = soup.find_all("div", class_="mr-2")
        for item in v_divs:
            if (find_version.search(item.get_text()) is not None):
                return True
            else:
                return False

    def __str__(self):
        return f"Looking for mod updates in Minecraft Version: {self.version}"
