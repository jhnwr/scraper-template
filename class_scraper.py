from requests_html import HTMLSession

class Scraper:
    def __init__(self):
        self.session = HTMLSession()
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}
        self.baseurl = 'https://www.amazon.co.uk/dp/'

    def extract(self, asin):
        r = self.session.get(self.baseurl + str(asin), headers=self.headers)
        scraped_item = (
            asin,
            'Amazon',
            r.html.find('span#productTitle', first=True).text,
            r.html.find('span#priceblock_ourprice', first=True).text,
        )
        return scraped_item



# testing
if __name__ == '__main__':
    plzsub = Scraper()
    prod = plzsub.extract('B08WX6ZDTY')
    print(prod)

