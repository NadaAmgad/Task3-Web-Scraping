import scrapy
import pandas as pd
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector

class MovieSpider(scrapy.Spider):
    name = "MovieSpider"
    url = "https://www.moviemeter.com/movies/top-250-best-movies-of-all-time"
    scraped_movies= []
    
    def start_requests(self):
        yield scrapy.Request( url = self.url, callback = self.parse )
    
    def parse(self, response):
        parse_movie_list = response.xpath('//*[@id="filter_system"]/div[2]/table/tbody/tr').getall()
        for movie in parse_movie_list:
            name_year = Selector(text=movie).xpath('//a/text()').get()
            name = name_year[:-7]
            year = name_year[-5:-1]
            alt_name =  " "
            if Selector(text=movie).xpath('//div[@class="sub altTitel"]/text()').get():
                alt_name = Selector(text=movie).xpath('//div[@class="sub altTitel"]/text()').get()[19:]
            scraped_movie = {
                'Name' : name,
                'Alt Name' : alt_name,
                'Year' : year,
                'Genre' : Selector(text=movie).xpath('//div[@class="sub"][1]/text()').get(),
                'Duration' : Selector(text=movie).xpath('//div[@class="sub"][2]/text()').get(),
                'Moviemeter Rank' : Selector(text=movie).xpath('//span/text()').get(),
                'Moviemeter Rating' : Selector(text=movie).xpath('//td[4]/div/div[1]/text()').get()
            }
            self.scraped_movies.append(scraped_movie)
            

    def closed(self,reason):
        df = pd.DataFrame(self.scraped_movies)
        df.to_csv('movie_data_moviemeter.csv', index=False)

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(MovieSpider)
process.start()