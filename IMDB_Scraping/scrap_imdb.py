import re
import scrapy
import pandas as pd
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector

# Website 2 - IMDB Top 250 movies

class ImdbMovieSpider(scrapy.Spider):

    # Empty list to which the dictionaries of extracted data will be appended
    top_250_movies = []

    name = "MovieSpider"

    # start_requests method
    def start_requests(self):
        yield scrapy.Request( url = "http://top250.info/charts/?2023/09/25", callback = self.parse )
        
    # parse method
    def parse(self, response):
        
	# Create an extracted list of the second table as there was a problem in extracting 
	# the data of <tr> tags
        list_of_table = response.xpath('/html/body/div[4]/table[2]').getall()

	#splitting the list of table at </tr> into multiple items to reach the required tags
        list_of_movies = [j.strip() for i in list_of_table for j in i.split('</tr>')]
        
        print(list_of_movies)
	
	# Removing the 1st and last elements in the list since they are of no importance
        last_in_list = list_of_movies.pop()
        first_in_list = list_of_movies.pop(0)
       
        print(list_of_movies)

	# Looping on the list of movies to extract the required data
        for movie in list_of_movies:
            movie_title = Selector(text = movie).xpath('//td[3]/a/span/text()').get()

	    # Extractiong the year from the title using regular expressions
            year = re.findall("\d{4}",movie_title)
	
	    # Extracting only the movie name from the title 
            movie_name = movie_title[:-7]
            current_movie = {'Name' : movie_name,
                             'IMDB Rank' : Selector(text = movie).xpath('//td[1]/text()').get(),
                             'IMDB Rating' : Selector(text = movie).xpath('//td[4]/text()').get(),
                             'Movie Year' : int(year[0])
                            }
            self.top_250_movies.append(current_movie)

        print(self.top_250_movies)  

    def closed(self,reason):
	# Creating Dataframe of Extracted Data
        top_250_movies_dataframe = pd.DataFrame.from_dict(self.top_250_movies)

	# Converting to CSV
        top_250_movies_dataframe.to_csv('movie_data_imdb.csv',index=False)


process = CrawlerProcess()
process.crawl(ImdbMovieSpider)
process.start()